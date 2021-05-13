N = int(input())
*A, = map(int, input().split())


d = {}


for i in range(N):
    if A[i] in d:
        d[A[i]] += 1
        continue
    d[A[i]] = 1

d = sorted(d.items(), reverse=True)

a = []

for key, data in d:
    if data>=4:
        a.append(key)
        a.append(key)
    elif data>=2:
        a.append(key)

if len(a)>=2:
    print(a[0]*a[1])
else:
    print(0)