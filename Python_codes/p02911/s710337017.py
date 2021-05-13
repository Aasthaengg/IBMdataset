n,k,q= map(int, input().split())
list1=[0]*n
for i in range(q):
  a=int(input())-1
  list1[a]+=1
for per in list1:
  if per >q-k:
    print('Yes')
  else:
    print('No')