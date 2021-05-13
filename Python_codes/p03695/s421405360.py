N=int(input())
A=list(map(int,input().split()))
S=set()
cnt=0
for i in A:
  if i>=3200:
    cnt+=1
  else:
    S.add(i//400)
if len(S)==0:
  low=1
  high=cnt
else:
  low=len(S)
  high=cnt+low
print(low,high)