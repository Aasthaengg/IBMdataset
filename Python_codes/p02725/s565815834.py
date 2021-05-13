k,n=map(int,input().split())
l=list(map(int,input().split()))
l.append(k+l[0])
max=0
for i in range(n):
  if l[i+1]-l[i]>max:
    max=l[i+1]-l[i]
print(k-max)