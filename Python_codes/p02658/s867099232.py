import sys
n = int(input())
a = list(map(int,input().split()))

m=1
l=10**18

if a.count(0) >= 1:
    print(0)
    sys.exit()

for i in range(n):
    m=m*a[i]
    if m > l:
        print(-1)
        sys.exit()

print(m)
