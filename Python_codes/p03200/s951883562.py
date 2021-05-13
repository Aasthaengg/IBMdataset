def rle(t):
    tmp2, num, ans = t[0], 1, []
    for i in range(1, len(t)):
        if tmp2 == t[i]:
            num += 1
        else:
            ans.append([tmp2, num])
            tmp2 = t[i]
            num = 1
    ans.append([tmp2, num])
    return ans


S = input()

s = list(map(str, S))
l = rle(S)
now = [[], [], []]
for i in range(len(S)):
    if S[i] == 'B':
        now[0].append(i)
for j in range(len(now[0])):
    now[1].append(len(S) - len(now[0]) + j)
    now[2].append(now[1][j] - now[0][j])
print(sum(now[2]))
