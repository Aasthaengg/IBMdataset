import sys

N = int(input())
A = list(map(int, input().split()))

if(0 in A):
    print(0)
    sys.exit(0)

prod = 1
for a in A:
    prod *= a
    if prod > 1000000000000000000:
        print(-1)
        sys.exit(0)

print(prod)