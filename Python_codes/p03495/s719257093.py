n,k=map(int,input().split())
nm=[0 for i in range(200010)]
a=list(map(int,input().split()))
for i in a:
  nm[i]+=1
nm.sort(reverse=True)
for i in range(k):
  n-=nm[i]
print(n)