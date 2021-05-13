N, K = [int(i) for i in input().split(' ')]

result = K 
for i in range(N-1):
    result *= K -1

print(result)
