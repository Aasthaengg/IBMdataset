n = int(input())
x = list(map(int, input().split()))
hp_min = 10000 * n
for i in range(1, 101):
    hp = sum([(x[j] - i) ** 2 for j in range(len(x))])
    if hp < hp_min:
        hp_min = hp
print(hp_min)
