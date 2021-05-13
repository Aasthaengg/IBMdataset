n=int(input())
A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
ans=[0]*n
for i in range(n):
  ans[i] += sum(A1[:i+1])+sum(A2[i:])
print(max(ans))