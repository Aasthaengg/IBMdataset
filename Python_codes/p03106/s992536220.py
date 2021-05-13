A, B, K = map(int, input().split())

count = 0
for i in range(1, 100):
    if A % i == 0:
        sho = A / i
        if B % sho == 0:
            count += 1
    if count == K:
        print(int(sho))
        break