N, K = map(int, input().split())
num = list(range(N+1))
count = 0
base_minimum = sum([i for i in num[:K]])
base_maximum = sum([i for i in num[-K:]])
count += base_maximum - base_minimum + 1

for k in range(K, N+1):
    base_minimum += num[k]
    base_maximum += num[-k-1]
    count += base_maximum - base_minimum + 1
    
print(int(count%(1e9+7)))