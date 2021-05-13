N=int(input())
list=[]
for i in range(N):
  a,b=map(int,input().split())
  list.append((b,a))
list.sort()
acc=0
for i in range(N):
  acc+=list[i][1]
  if acc>list[i][0]:
    print('No')
    exit()
print('Yes')