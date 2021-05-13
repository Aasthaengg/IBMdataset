N = int(input())
A = list(map(int,input().split()))
ans = 0
tmp = 0
prev = -1
for a in A:
  if prev<a:
    ans = max(tmp, ans)
    tmp = 0
  else:
    tmp+=1
  prev = a
ans = max(ans,tmp)
print(ans)