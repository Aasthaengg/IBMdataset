N=int(input())
A= list(map(int,input().split()))
l=[0]*N
for i in range(N):
   if A[i] == i+1:
      l[i]=1
ans=0
for i in range(N):
   if l[i] == 1:
      try:
         if l[i+1] == 1:
            l[i+1]=0
            ans+=1
         else:
            ans+=1
      except IndexError:
         ans+=1
print(ans)