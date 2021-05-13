N = int(input())
x = {}
for _ in range(N):
    s = input()
    if s in x:
        x[s] += 1
    else:
        x[s] = 1

maxcount = max(x.values())
ans = []
for s, count in x.items():
    if count == maxcount:
        ans.append(s)
ans.sort()
for a in ans:
    print(a)