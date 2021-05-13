mod = 10**9+7
n,k = map(int,input().split())
a = list(map(int,input().split()))
sub,inv = 0,0
for i in range(n):
  for j in range(n):
    if a[j] > a[i]:
      if i < j:
        sub+=1
      inv+=1
print(((inv*(k*(k+1))//2)-(sub*k))%mod)