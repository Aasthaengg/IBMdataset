#ABC 084 D - 2017 Like Number
from itertools import accumulate

def isPrime(x):
    if x == 2: flag = True
    else:
        flag = True
        if x % 2 == 0:
            flag = False
        
        i = 3
        while i**2 <= x and flag == True:
            if x % i == 0:
                flag = False
            else:
                i += 2
    return True if flag == True else False

q = int(input())
arr = []
max_v = 0
for i in range(q):
    l,r = map(int, input().split())
    arr.append((l,r))
    max_v = max(max_v, r)

res_arr = [0]*(max_v+1)
for i in range(3,max_v+1,2):
    v1, v2 = i, (i+1)//2
    if isPrime(v1) == True and isPrime(v2) == True:
        res_arr[i] = 1

cumsum = list(accumulate(res_arr))
#print(res_arr)
#print(cumsum)
for i in range(q):
    l,r = arr[i][0], arr[i][1]
    print(cumsum[r] - cumsum[l-1])