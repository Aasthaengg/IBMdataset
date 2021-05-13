S = input().rstrip()
T = []
cnt = 0
for s in S:
    if not T:
        T.append(s)
        continue
    if s!=T[-1]:
        cnt += 2
        T.pop()
    else:
        T.append(s)
print(cnt)