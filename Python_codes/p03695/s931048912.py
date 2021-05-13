n = int(input())
colors = [0]*8
gold = 0
for a in map(int, input().split()):
    color = a//400
    if 8 <= color:
        gold += 1
        continue
    colors[color] = 1
print(max(sum(colors), 1), sum(colors)+gold)
