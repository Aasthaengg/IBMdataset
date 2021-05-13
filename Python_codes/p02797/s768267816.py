n,k,s = map(int,input().split())
if s != 10**9:
    ans = [str(s)]*k + [str(10**9)]*(n-k)
else:
    ans = [str(s)]*k + [str(1)]*(n-k)
print(" ".join(ans))