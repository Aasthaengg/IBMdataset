n = int(input())
x = list(map(int, input().split()))
xs = sorted(x)

default = (n+1)//2

for i in range(n):
    if x[i] >= xs[(n+1)//2]:
        print(xs[n//2-1])
    else:
        print(xs[n//2])

