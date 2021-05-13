
N, M = map(int, input().split())

divisor = []
for i in range(1, int(M ** 0.5) + 1):
    if M % i == 0:
        divisor.append(i)
        if i != M // i:
            divisor.append(M // i)

print(max(filter(lambda x: x <= M // N, divisor)))
