K,R = map(int,input().split())

if(K >= 10):
  ans = R
else:
  ans = R  + 100*(10-K)
print(ans)  