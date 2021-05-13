N=int(input())
A= list(map(int,input().split()))
sum_A=sum(A)
B= list(map(int,input().split()))
ans=0
if sum_A < sum(B):
   print(-1)
   exit()
l=[]
S=0
for i in range(N):
   if A[i]<B[i]:
      ans+=1
      S+=B[i]-A[i]
   elif A[i]>=B[i]:
      l.append(A[i]-B[i])
l.sort(reverse=True)
cnt=0
for i in l:
   if S>0:
      S-=i
      cnt+=1
print(ans+cnt)