N = int(input())
divisors = []
for i in range(1,int(N**0.5)+1):
    #print(i)
    if N%i == 0:
        divisors.append(i)
        divisors.append(N//i)
divisors.remove(1)
ds = set(divisors)
ans = 0
for div in ds:
    if div == 1:
        continue

    if N//(div-1) == N%(div-1):
        ans += div-1
print(ans)