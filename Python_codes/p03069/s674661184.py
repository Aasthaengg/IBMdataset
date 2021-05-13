from itertools import groupby

N = int(input())
S = input()

l = [[i, len(list(j))] for i, j in groupby(S)]

w = 0
bl = 0
for i in S:
    if i == ".":
        w += 1
    else:
        bl += 1

ans = [w, bl]
cnt = 0
for i, j in l:
    if i == ".":
        w -= j
        ans.append(cnt + w)
    else:
        cnt += j
        ans.append(cnt + w)
        
print(min(ans))