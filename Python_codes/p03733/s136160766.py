N, T = map(int, input().split())
t = list(map(int, input().split()))

print(sum(min(T, t[i+1] - t[i]) for i in range(N-1)) + T)
