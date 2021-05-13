n=int(input())
l=list(map(int,input().split()))
bitlist=[]
for i in range(n):
  bit=[]
  num=l[i]
  for j in range(20):
    bit.append(num%2)
    num//=2
  bitlist.append(bit)
left=0
right=0
b=True
ans=1
now={}
for i in range(20):
  if bitlist[0][i]==1:
    now[2**i]=1
  else:
    now[2**i]=0
b=1#b=1の時右を伸ばす
while right<n:
  if b==1:
    right+=1
    if right==n:
      break
    for i in range(20):
      if bitlist[right][i]==1:
        now[2**i]+=1
        if now[2**i]>=2:
          b=0
    if b==1:
      ans+=right-left+1
  else:
    b1=1
    for i in range(20):
      if bitlist[left][i]==1:
        now[2**i]-=1
      if now[2**i]>=2:
        b1=0      
    left+=1
    if b1==1:
      b=1
      ans+=right-left+1
print(ans)