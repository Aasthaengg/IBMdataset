n, m = (int(x) for x in input().split())
s = input()
t = list(reversed(s))

ANS = []
i = 0
while i < n:
    for j in reversed(range(1, m+1)):
        if i+j > n:
            continue
        else:
            if t[i+j] == "1":
                continue
            else:
                ANS.append(j)
                i += j
                break
    else:
        print(-1)
        exit()

print(*reversed(ANS))