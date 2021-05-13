import collections

N = int(input())

a = []
b = []
for i in range(N):
    s = input()
    a.append(s)

M = int(input())
for i in range(M):
    t = input()
    b.append(t)

a1 = collections.Counter(a)
a2 = a1.most_common()

ans = 0
for i in range(len(a1)):
    total = a2[i][1] - b.count(a2[i][0])
    if total > ans:
        ans = total
    else:
        continue
print(ans)