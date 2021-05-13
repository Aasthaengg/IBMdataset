N, _ = map(int, input().split())
A = sum(map(int, input().split()))
print(N-A) if N >= A else print(-1)