s = int(input())
DP = [s]
S = set()
S.add(s)
cnt = 1
while True:
    cnt += 1
    if DP[-1] % 2 == 0:
        x = DP[-1] // 2
    else:
        x = DP[-1] * 3 + 1
    if x in S:
        break
    S.add(x)
    DP.append(x)


print(cnt)