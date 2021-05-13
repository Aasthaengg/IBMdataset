A,B,C,N= list(map(int,input().split()))
ans=0
for i in range(0,N//A+1):
   for j in range(0,(N-i*A)//B+1):
      if (N-i*A-j*B)%C==0:
         ans+=1
print(ans)