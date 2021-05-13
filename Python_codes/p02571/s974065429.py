s = list(input())
t = list(input())

maxx = 0

for i in range(len(s) - len(t) + 1):
    ppp = 0
    for j in range(len(t)):
        if s[i + j] == t[j]:
            ppp += 1
    if ppp > maxx:
        maxx = ppp

print(len(t) - maxx)
