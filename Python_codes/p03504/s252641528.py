N,C=[int(x) for x in str(input()).split()]
A=[]
for i in range(N):
  a,b,d=[int(x) for x in str(input()).split()]
  A.append([d,a,b])


br=200002

count=[0 for i in range(br)]

A.sort()
for i in range(1,C+1):
  ind=[0 for i in range(br)]
  end=0
  for j in range(N):
    if A[j][0]==i:
      if end!=A[j][1]:
        end=A[j][2]
        ind[2*A[j][1]-1]=1
        ind[2*end]=-1
      else:
        end=A[j][2]
        ind[2*A[j][1]]=0
        ind[2*end]=-1
  temp=0
  for j in range(br):
    temp+=ind[j]
    if temp>0:
      count[j]+=1

print(max(count))










