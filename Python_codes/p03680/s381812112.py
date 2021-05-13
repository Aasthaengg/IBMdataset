s = input()
n = int(s)

nodes = []

for i in range(n):
    p = input()
    q = int(p)
    nodes.append(q)

answer = -1
m = []

x = nodes[0]
m.append(x)
for i in range(n-1):
    w = nodes[x-1]
    m.append(w)
    x = w

for i in range(len(m)):
    if m[i] == 2:
        answer = i + 1
        break

print(answer)
