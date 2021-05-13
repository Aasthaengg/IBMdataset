n=int(input())
L=list(map(int,input().split()))
cnt=0
ok=1
while ok:
  for i in range(n):
    if L[i]%2==1:
      ok=0
      break
    L[i]/=2
  if ok:cnt+=1

print(cnt)