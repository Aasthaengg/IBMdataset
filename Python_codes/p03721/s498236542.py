N, K = [int(x) for x in input().split()]

result = {}
for _ in range(N):
    a, b = [int(x) for x in input().split()]
    if a in result:
        result[a] += b
    else:
        result[a] = b

result = sorted(result.items())

now = 0
for key, value in result:
    now += value

    if now >= K:
        print(key)
        exit()
