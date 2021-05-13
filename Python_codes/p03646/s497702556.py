K = int(input())
N = 50

a = [i for i in range(N)]
a = [x + K // N for x in a]
for i in range(K % N):
    a = [x - 1 for x in a]
    a[i] += N + 1

print(N)
print(*a)
