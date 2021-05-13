n,k=list(map(int,input().split()))
s=input()

if s[0]=='0':
    seq=[0]
else:
    seq=[]

i=0
while i<n:
    j=i
    while j<n and s[j]==s[i]:
        j+=1
    seq.append(j-i)
    i=j

if s[-1]=='0':
    seq.append(0)

bleft=0
bright=min(2*k,len(seq)-1)

cursum=sum(seq[bleft:bright+1])
ret=cursum

for i in range(2,len(seq),2):
    left=i
    right=min(i+2*k,len(seq)-1)

    if bleft!=left:
        cursum-=seq[bleft]+seq[bleft+1]
        bleft=left
    if bright!=right:
        cursum+=seq[right-1]+seq[right]
        bright=right
    
    ret=max(ret,cursum)
    
print(ret)
