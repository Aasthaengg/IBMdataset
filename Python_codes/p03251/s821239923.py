N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

ans = 'War'

for z in range(X+1, Y+1):
    if len(list(filter(lambda x: x < z, x))) == N and len(list(filter(lambda x: x >= z, y))) == M:
        ans = 'No War'
        break

print(ans)
