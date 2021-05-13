n=int(input())
L=list(map(int,input().split()))
cnt=0
for i in range(n):
  for j in range(i):
    for k in range(j):
      if (L[i]!=L[j] and L[j]!=L[k] and L[i]!=L[k]) and (L[i]+L[j]>L[k] and L[j]+L[k]>L[i] and L[k]+L[i]>L[j]):
        cnt+=1
print(cnt)
