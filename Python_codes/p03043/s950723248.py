import math
N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    num_success = max(0,math.ceil(math.log2(K / i)))
    ans += (1 / 2) ** num_success
   
print(ans / N)
        
