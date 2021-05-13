import sys
input = sys.stdin.readline
Q = int(input())

#nの素数判定
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

l = [0]*(10**5+1)
for i in range(1, 10**5+1):
    if i%2 and is_prime(i) and is_prime((i+1)//2):
        l[i] = 1

for i in range(len(l)-1):
    l[i+1] += l[i]

for _ in range(Q):
    ll, rr = map(int, input().split())
    print(l[rr]-l[ll-1])