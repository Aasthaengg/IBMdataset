A,B,C,K = map(int,input().split())
ans = A-B
if abs(ans) > 10**18:
  ans = 'Unfair'
else:
  if K%2 != 0:
    ans = B-A
print(ans)