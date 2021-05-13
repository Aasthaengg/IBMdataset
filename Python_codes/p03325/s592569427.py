N=int(input())
a=list(map(int, input().split()))
ct=0
for i in range(N):
  k=0
  while a[i]%2==0:
    k+=1
    a[i]//=2
  ct+=k
print(ct)