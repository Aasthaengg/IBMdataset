MOD=10**9+7
N=int(input())
A=list(map(int, input().split()))

huts=[0, 0, 0]
out=1
for i in range(N):
  out*=huts.count(A[i])
  if out==0:
    print(0)
    exit()
  huts[huts.index(A[i])]+=1
print(out%MOD)