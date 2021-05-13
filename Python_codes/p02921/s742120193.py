S = input()
T = input()

cnt, i = 0, 0

for s in S:
    if s == T[i]:
        cnt += 1
    i += 1

print(cnt)