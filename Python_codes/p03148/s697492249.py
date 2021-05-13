n, k = map(int, input().split())
td = list(sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda td: -td[1]))
td2 = []
eaten = set()
dup = 0
score = k * k
i = 0
j = 0
while len(eaten) + dup < k:
    if i < n and td[i][0] in eaten:
        td2.append(td[i])
        i += 1
    else:
        diff = (k - dup) * (k - dup) - (k - dup - 1) * (k - dup - 1)
        if i < n and (j >= len(td2) or td[i][1] >= td2[j][1] - diff):
            t, d = td[i]
            score += d
            eaten.add(t)
            i += 1
        else:
            t, d = td2[j]
            score += d - diff
            dup += 1
            j += 1
print(score)
