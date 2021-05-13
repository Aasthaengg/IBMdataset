N,M=list(map(int,input().split()))
def div(N):
   l=[]
   for i in range(1,int(N**0.5)+1):
      if N%i==0:
         l.append(i)
         if i != N//i:
            l.append(N//i)
   l.sort()
   return l
l = div(M)
ans=-1
for i in l:
   if M//i>=N:
      ans+=1
   else:
      break
print(l[ans])