n = int(input())
card = {}
for _ in range(n):
    t = input()
    if t not in card:
        card[t] = 1
    else:
        card[t] += 1
m = int(input())
for _ in range(m):
    t = input()
    if t not in card:
        card[t] = 1
    else:
        card[t] -= 1

ans = 0

for i in card.values():
    if i > ans:
        ans = i

print(ans)
