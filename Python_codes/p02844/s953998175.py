from collections import defaultdict

N = int(input())
S = input()

d = defaultdict(list)
for i, s in enumerate(S):
    d[s].append(i)
ans = 0

for i in range(1000):
    T = '%03d' % i
    j = -1
    for t in T:
        flag = True
        for k in d[t]:
            if k > j:
                flag = False
                j = k
                break
        if flag:
            break
    if not(flag):
        ans += 1

print(ans)