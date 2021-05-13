N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=[]
cnt=0
fusoku=0 #正の値とする
for i in range(N):
  C.append([A[i],B[i],A[i]-B[i]])
  if A[i]-B[i]<0:
    cnt += 1
    fusoku += abs(A[i]-B[i])
    
#print(C)
#print(fusoku)
  
if sum(A)<sum(B):
  print(-1)
else:
  C.sort(key=lambda x:x[2],reverse=True)
  for t in C:
    if fusoku<=0:
      break
    else:
      cnt +=1
      fusoku -= t[2]
  print(cnt)