
max2 = lambda x,y: x if x > y else y
min2 = lambda x,y: x if x < y else y

s = input()
N = len(s)

indices = [[] for _ in range(26)]

for i,c in enumerate(s):
    indices[ord(c)-ord('a')].append(i)


res = N-1
for l in indices:
    if not l:
        continue

    t = 0
    for a,b in zip([-1]+l,l+[N]):
        t = max2(t,b-a-1)
    res = min2(res, t)

print(res)