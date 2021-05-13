k,n = map(int,input().split())
ans =[]
for i in range(1,k):
  ans.append(n+i)
  ans.append(n-i)
ans.append(n)
ans.sort()
ans = list(map(str,ans))
print(" ".join(ans))