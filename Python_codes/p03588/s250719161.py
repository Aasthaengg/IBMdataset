N = int(input())

mini = [10 ** 10, -1]
for _ in range(N):
    a, b = map(int, input().split())
    if mini[0] > b:
        mini[0] = b
        mini[1] = a

print(mini[1] + mini[0])
