n = int(input())
count = {}
for i in range(n):
    s = input()
    if s in count:
        count[s] += 1
    else:
        count[s] = 1
m = int(input())

for i in range(m):
    t = input()
    if t in count:
        count[t] -= 1
    else:
        count[t] = -1
max_v = max(count.values())
if max_v < 0:
    max_v = 0
print(max_v)