S = input()
c = 0
stone = S[0]
for s in S:
    if stone != s:
        stone = s
        c += 1
print(c)