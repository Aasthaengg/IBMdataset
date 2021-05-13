N=int(input())
H=list(map(int,input().split()))

ans = 0
c = 0
for i,h in enumerate(H[:-1]):
  if h >= H[i+1]:
    c += 1
  else:
    ans = max(ans,c)
    c = 0
ans = max(ans,c)
print(ans)