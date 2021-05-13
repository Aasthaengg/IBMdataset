n,k,q=map(int,input().split())
ans = [k-q]*n
for i in range(q):
  ans[int(input())-1]+=1
for i in range(n):
  print("Yes" if ans[i]>0 else "No")