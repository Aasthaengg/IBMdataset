N, M ,C = map(int, input().split())
B = list(map(int, input().split()))
n = 0
for i in range(N):
    a = list(map(int, input().split()))
    AB = [x * y for (x, y) in zip(a,B)]

    if sum(AB) > -C:
        n += 1

print(n)
