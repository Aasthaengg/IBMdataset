s = input()
t = input()
N, M = len(s), len(t)

schr, indchr = dict(), dict()
for i in range(N):
    if s[i] in schr:
        schr[s[i]].append(i+1) 
    else:
        schr[s[i]] = [i+1]
        indchr[s[i]] = 0

schrset = set(schr)
ans, pos, pre, back = 0, 0, set(), True
for i in range(M):
    if t[i] in schrset:
        c = schr[t[i]]
        if c[-1] <= pos:
            ans += N - pos + c[0]
            pos = c[0]
            if not back:
                for x in indchr.keys():
                    indchr[x] = 0
                back, pre = True, set()
        else:
            j = indchr[t[i]]
            while c[j] <= pos:
                j += 1
            if j > 0:
                pre.add(t[i])
            ans += c[j] - pos
            pos, back, indchr[t[i]] = c[j], False, j
    else:
        print(-1)
        exit()
print(ans)