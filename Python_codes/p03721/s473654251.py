N, K = map(int, input().split())

AB = [[] for _ in range(N)]

for i in range(N):
    AB[i] = list(map(int, input().split()))

AB = sorted(AB)
mem = K
for ab in AB:
    a = ab[0]
    b = ab[1]
    mem -= b
    if mem <= 0:
        print(a)
        break