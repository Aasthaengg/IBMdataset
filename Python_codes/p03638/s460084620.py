h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
A=[]
for i in range(n):
  for j in range(a[i]):
    A.append(i+1)
ans=[[0]*w for i in range(h)]
for i in range(h):
  ans[i]=A[i*w:(i+1)*w]
for i in range(1,h,2):
  ans[i]=ans[i][::-1]
for i in range(h):
  for j in range(w):
    print(ans[i][j],end=" ")
    if j==w-1:
      print()