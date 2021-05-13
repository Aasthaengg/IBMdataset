N=int(input())
A=[0]*N
B=[0]*N
diff=[0]*N
for i in range(N):
  A[i],B[i]=map(int,input().split())
  diff[i]=[A[i]+B[i],i]
  
diff=sorted(diff,key=lambda x:x[0])[::-1]
taka=0
aoki=0
for i in range(len(diff)):
  if i%2==0:
    taka+=A[diff[i][1]]
  else:
    aoki+=B[diff[i][1]]

print(taka-aoki)