K,T=map(int,input().split())
a=list(map(int,input().split()))
while len(a)>1:
  a.sort(reverse=True)
  a[0]-=a.pop()
print(max(0,a[0]-1))