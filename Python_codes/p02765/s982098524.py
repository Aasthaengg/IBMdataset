n,r = map(int,input().split())
print(r if 10 <= n else r + 1000 - 100*n)