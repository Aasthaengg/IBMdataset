n, m = [int(w) for w in input().split()]
menu = [0] * m

for i in range(n):
    _, *la = [int(w) for w in input().split()]
    for a in la:
        menu[a - 1] += 1

print(len([w for w in menu if w == n]))
