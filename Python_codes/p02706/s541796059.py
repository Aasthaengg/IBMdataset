N, M = map(int, input().split())
As = list(map(int, input().split()))
preans = sum(As)
if preans <= N:
    print(N - preans)
else:
    print(-1)