N, K = list(map(int,input().split()))

mod = 10**9 + 7
array = []

for k in range(1, K+1):
    array.append(pow((K // k), N, mod))
    
for k in range(K, 0, -1):
    for i in range(2*k, K+1, k):
        array[k-1] -= array[i-1]

sum = 0
for k in range(1, K+1):
    array[k-1] *= k
    array[k-1] %= mod
    sum += array[k-1]
    
sum %= mod

print(sum)