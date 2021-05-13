N = int(input())
MOD = 10**9 + 7

prime=[]
for n in range(2, 1001):
    for i in range(2,n):
        if n % i == 0:
            break
    else:
        prime.append(n)
#print(prime)

bucket={}
for p in prime:
    bucket[p]=0
#print(bucket)

for i in range(2, N+1):
    for p in prime:
        if p > i:
            break
        #print(i,p)
        while i % p == 0:
            i //= p
            bucket[p] += 1

#print(bucket)

ans=1
for p in prime:
    ans = (ans * (bucket[p] + 1)) % MOD

print(ans)

