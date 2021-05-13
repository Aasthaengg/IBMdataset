K = int(input())

N = 50
x = [v + K // N for v in range(N)]
for i in range(K % N):
    for j in range(N):
        if j == i:
            x[j] += N
        else:
            x[j] -= 1
            
print(N)
print(*x)
