n,k,s = map(int,input().split())
if s == 10**9:
  b = ['1']
else:
  b = [str(s+1)]

ans = [str(s)]*k + b*(n-k)
print(' '.join(ans))