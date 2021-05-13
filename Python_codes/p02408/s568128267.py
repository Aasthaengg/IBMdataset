n = int(input())
cards = []
for i in range(n):
    s, a = input().split()
    cards.append((s, int(a)))
l = [(s, a) for s in "SHCD" for a in range(1,14) if (s,a)not in cards]
for s, a in l:
    print(s + " " + str(a))