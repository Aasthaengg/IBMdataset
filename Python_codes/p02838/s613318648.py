MOD = 10**9 + 7

N = int(input())
A = list(map(int, input().split()))

num_per_digit = [0]*60

for i in range(60):
    num = 0
    for j,a in enumerate(A):
        num += a % 2
        A[j] //= 2
    num_per_digit[i] = num

result = 0    
for d,num in enumerate(num_per_digit):
    result = (result + num * (N - num) * pow(2, d, MOD)) % MOD
    
print(result)