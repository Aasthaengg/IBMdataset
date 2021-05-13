n=int(input())
p=[int(input()) for i in range(n)]
q=[0]*n

cnt=0
maxcnt=0


for i in range(n):
  q[p[i]-1]=i+1

for i in range(n-1):
  if q[i]<q[i+1]:
    cnt+=1
    maxcnt=max(maxcnt,cnt)
  else:
    cnt=0

print(n-maxcnt-1)