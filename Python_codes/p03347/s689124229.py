n=int(input())
A=[]
for i in range(n):
  A.append(int(input()))
ans=0
chk=True
cur=0
for i in reversed(range(n)):
  if A[i]==cur:
    cur-=1
    continue
  else:
    if A[i]>i or A[i]<cur:
      chk=False
    else:
      ans+=A[i]
      cur=A[i]-1
print(ans if chk else -1)