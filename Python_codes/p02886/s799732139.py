n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(len(l)):
  for j in range(i):
    res=l[i]*l[j]
    s+=res
print(s)