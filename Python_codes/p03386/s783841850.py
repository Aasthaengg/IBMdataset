A,B,K = map(int,input().split())
ans = []
for i in range(A,A+K):
  if i <= B:
    ans.append(i)
#print(ans)
for j in range(B,B-K,-1):
  #print("j",j)
  if j >= A+K:
    ans.append(j)
ans.sort()
for k in ans:
  print(k)
