N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A_sum=0
for i in range(N):
   if A[i]>B[i]:
      A_sum+=A[i]-B[i]
   elif A[i]<B[i]:
      A_sum-=(B[i]-A[i])//2
if A_sum<=0:
   print("Yes")
else:
   print("No")
