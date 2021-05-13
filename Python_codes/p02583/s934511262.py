N=int(input())
l=list(map(int, input().split()))
s=0
for i in range(N):
  for j in range(N):
    for k in range(N):
      if l[i]!=l[j] and l[j]!=l[k] and l[k]!=l[i] and l[i]<l[j]+l[k] and l[j]<l[i]+l[k] and l[k]<l[i]+l[j]:
        s+=1
print(int(s/6))
