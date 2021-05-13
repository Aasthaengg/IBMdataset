N,M = map(int,input().split())
conflict = []
for _ in range(M):
    a,b = map(int,input().split())
    conflict.append((a,b))

conflict.sort(key=lambda x: x[1])
count = 0
t = -1
for a,b in conflict:
    if t <= a:
        count += 1
        t = b
print(count)