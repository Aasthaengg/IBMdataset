n,k=map(int,input().split())
A=list(map(int,input().split()))
ans = [0]*(n)
for a in A:
  ans[a-1] += 1
ans.sort(reverse=True)
print(sum(ans[k:]))