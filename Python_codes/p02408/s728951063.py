mark = ["S", "H", "C", "D"]
cards = []
for m in mark:
    for i in range(1, 14):
        cards.append(m + " " + str(i))
n = int(input())
for j in range(n):
    cards.remove(input())

for c in cards:
    print(c)