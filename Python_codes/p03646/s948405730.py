K = int(input())
N = 50
a = [0] * N
for i in range(K % N):
    a[i] = N-1-K+(N+1)*(K//N+1)
for i in range(K % N, N):
    a[i] = N-1-K+(N+1)*(K//N)
print(N)
print(' '.join(map(str, a)))
