N=int(input())
AB=[]
for i in range(N):
  a,b=map(int,input().split())
  AB.append((a,b))

AB = sorted(AB,key=lambda x:x[1])
t=0
for i in range(N):
  ab=AB[i]
  t += ab[0]
  if t > ab[1]:
    print('No')
    exit()
print('Yes')