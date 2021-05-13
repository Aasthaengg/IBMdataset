A=int(input())
def divisor_enu(N):
   S=1
   for i in range(2,int(N**0.5)+1):
      cnt=0
      if N%i==0:
         while N%i==0:
            cnt+=1
            N//=i
         S*=(cnt+1)
   if N != 1:
      S*=2
   return S
ans=0
for i in range(1,A+1):
   if divisor_enu(i)==8 and i%2==1:
      ans+=1
print(ans)