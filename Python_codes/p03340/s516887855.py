N=int(input())
A=list(map(int,input().split()))

def addable(a,b):
  if a<b:
    a,b=b,a
  sa=bin(a)[2:]
  sb=bin(b)[2:].zfill(len(sa))
  for i in range(len(sa)):
    if sa[i]=="1" and sb[i]=="1":
      return False
  return True
  
right=1
ans=0
cur=A[0]
for left in range(N):
  while right<N and addable(cur,A[right]):
    cur|=A[right]
    right+=1
  ans+=(right-left)
  
  if left==right:
    right+=1
  else:
    cur-=A[left]
  
print(ans)