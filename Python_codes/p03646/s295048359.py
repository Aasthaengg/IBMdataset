K = int(input())
N = 50
a = [N-1] * N
for _ in range(K % N):
    a.sort()
    for p in range(N):
        if a[p] + N >= a[N - 1] - 1:
            for i in range(N):
                if i == p:
                    a[i] += N
                else:
                    a[i] -= 1
            break
for i in range(N):
    a[i] += K // N
print(N)
print(" ".join(map(str, a)))