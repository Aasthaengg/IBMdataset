import collections
s = list(input())
t = list(enumerate(s[:]))
eng = [chr(ord('a') + i) for i in range(26)]
u = len(s)

ans = []
for i in eng:
    kar = [-1]
    kar.extend([j for j, v in t if v == i])
    kar.append(u)
    tyu = len(kar)
    if tyu == 2:
        continue
    f = 0
    for j in range(tyu-1):
        f = max(f,kar[j+1]-kar[j]-1)
    ans.append(f)

print(min(ans))