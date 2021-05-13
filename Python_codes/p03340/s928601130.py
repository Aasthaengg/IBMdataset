n=int(input())
arr=list(map(int,input().split()))
ans=0
pos=0
cnt=0
while 1:
  if pos==n:
    break
  if arr[pos]==0:
    cnt+=1
    pos+=1
    continue
  sum=0
  xor=0
  len=0
  for i in range(pos,n):
    if arr[i]==0:
      len+=1
      continue
    sum+=arr[i]
    xor=xor^arr[i]
    if sum!=xor:
      break
    len+=1
  ans+=len*(cnt+1)+(cnt*(cnt+1))//2
  cnt=0
  pos+=1
if cnt!=0:
  ans+=(cnt*(cnt+1))//2
print(ans)