N=int(input())
work=[0]*N
for i in range(N):
  work[i]=list(map(int,input().split()))
work=sorted(work,key=lambda x: x[1])
time=0
for i in work:
  time+=i[0]
  if time>i[1]:
    print('No')
    exit()
print('Yes')