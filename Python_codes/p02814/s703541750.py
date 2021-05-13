from fractions import gcd
n,m = map(int,input().split())
A = list(map(int,input().split()))

l = 1
cnt = -1
for a in A:
    l = l*a//gcd(l,a)
    i = 0
    while a%2 == 0:
        a = a//2
        i += 1
    if cnt == -1:
        cnt = i
    elif cnt != i:
        print(0)
        exit(0)

ans = 1 + (m - l//2)//l
print(ans)
