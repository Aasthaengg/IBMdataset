n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))

q = {0:0, 1:0, 2:0}
for i in p:
    if i <= a:
        q[0] += 1
    elif i >= b + 1:
        q[2] += 1
    else:
        q[1] += 1
print(min(q.values()))