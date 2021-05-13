N,M=map(int,input().split())
A=list(map(int,input().split()))
A[0]%=M
for i in range(N-1):
  A[i+1]+=A[i]
  A[i+1]%=M
d={}
for i in range(N):
  if A[i] in d:
    d[A[i]]+=1
  else:
    d[A[i]]=1
count=0

for k,v in d.items():
  count+=v*(v-1)/2
  if k==0:
    count+=v

print(int(count))