AB = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    AB.append([a, b])

AB = sorted(AB, key=lambda x: x[0], reverse=True)
print(sum(AB[0]))