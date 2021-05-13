n,k,s = map(int,input().split())
if s != int(1e9):
    ans = [s] * k + [int(1e9)] * (n-k)
else:
    ans = [int(1e9)] * k + [1] *(n-k)
print(*ans)
