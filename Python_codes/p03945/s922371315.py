S = input()

color = S[0]

cnt = 0

for c in S:
    if c != color:
        cnt += 1
        color = c

print(cnt)