N = int(input())
a = [set() for _ in range(N)]

for i in range(N):
    id = int(input()) - 1
    a[id].add(i)

step = -1
#already = a[1]
now = a[1]
next = set()
for i in range(N-1):
    #already = already.union(now)
    if 0 in now:
        step = i+1
        break
    for j in now:
        next = next.union(a[j])
    now = next
    next = set()

print(step)