point = [0, 0]
n = int(input())
for _ in range(n):
    cards = input().split()
    if cards[0] > cards[1]:
        point[0] += 3
    elif cards[0] < cards[1]:
        point[1] += 3
    else:
        point = [n + 1 for n in point]
print(*point)