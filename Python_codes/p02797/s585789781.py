A,B,N= list(map(int,input().split()))
l=[]
for i in range(B):
   l.append(N)
for i in range(A-B):
   l.append(N+1 if N != 1000000000 else 1000)
print(*l)