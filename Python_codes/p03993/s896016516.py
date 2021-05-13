N = int(input())
rabbit = list(map(lambda x: int(x) - 1, input().split()))

total = 0
for i in range(N):
    if rabbit[rabbit[i]] == i:
        total += 1

print(total // 2)