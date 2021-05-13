n,k = (int(i) for i in input().split())
mod = 10**9+7
list = [0]*(k+1)
ans = 0
for i in range(1,k+1):
	list[i] = pow((k//i),n,mod)

for i in range(k,0,-1):
	for j in range(2*i,k+1,i):
		list[i]-=list[j]


for i in range(k+1):
    ans += list[i] * i % mod

print(ans%mod)
