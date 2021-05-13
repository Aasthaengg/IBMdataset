n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

ddict = {}
for di in d:
    if di in ddict:
        ddict[di] += 1
    else:
        ddict[di] = 1

tdict = {}
for ti in t:
    if ti in tdict:
        tdict[ti] += 1
    else:
        tdict[ti] = 1

ans = True
for key, value in tdict.items():
    if key in ddict:
        if value > ddict[key]:
            ans = False
            break
    else:
        ans = False
        break

print("YES" if ans else "NO")