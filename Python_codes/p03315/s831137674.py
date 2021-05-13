S = input()
sm = 0
for a in S:
    if a == '+':
        sm += 1
    else:
        sm -= 1

print(sm)
