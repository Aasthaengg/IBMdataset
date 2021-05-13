a,b=map(int,input().split())
lst=[0 for _ in range(10**4,10**5)]

for i,_ in enumerate(lst):
  w=str(10**4+i)
  if w[0]==w[-1] and w[1]==w[-2]:
    lst[i]=1

print(sum(lst[a-10**4:b+1-10**4]))