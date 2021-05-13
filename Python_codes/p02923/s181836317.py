N=int(input())
H=list(map(int,input().split()))
count=0
maxcount=[0]*N
for i in range(N-1):
  if(H[i]>=H[i+1]):
    count+=1
  else:
    count=0
  maxcount[i]=count

print(max(maxcount))