n,m = map(int,input().split())
a = list(map(int,input().split()))

for h in a:
    n -= h
    if n < 0:
        print(-1)
        exit(0)

print(n)