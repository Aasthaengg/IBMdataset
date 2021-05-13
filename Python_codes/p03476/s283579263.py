import math
import bisect
def binary_search(a,n):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        index = a[mid]
        if index == n:
            return True
        elif index < n:
            low = mid+1
        else:
            high = mid -1
    return False

def get_sieve_oof_eratosthenes(n):
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1,n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]
data = get_sieve_oof_eratosthenes(10**5 + 1)
count = [0 for i in range(10**5+1)]
for i in range(3,10**5,2):
    if binary_search(data,i) and binary_search(data,(i+1)//2):
            count[i] += count[i-1] + 1
            count[i+1] = count[i]
    else:
        count[i] += count[i-1]
        count[i+1] = count[i]
q = int(input())
for i in range(q):
    l,r = map(int,input().split())
    print(count[r]-count[l-1])
