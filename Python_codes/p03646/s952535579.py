K = int(input())
N = 50
p = K // N
q = K % N
r = N - q
ans = [N-1+p - q]*r + [N-1+p + N-q+1]*q
print(N)
print(*ans)