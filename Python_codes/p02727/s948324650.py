X,Y,A,B,C = (int(x) for x in input().split())
p = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]
r = [int(x) for x in input().split()]

p = sorted(p, reverse=True)
q = sorted(q, reverse=True)
r = sorted(r, reverse=True)

p.append(0)
q.append(0)
r.append(0)
for i in range(X,A):
    p[i] = 0
for i in range(Y,B):
    q[i] = 0

a = 0
b = 0
c = 0
cnt = 0

for i in range(X+Y):
    if (not a == X) and p[a] >= q[b] and p[a] >= r[c]:
        cnt += p[a]
        a += 1
    elif (not b == Y) and q[b] >= r[c]:
        cnt += q[b]
        b += 1
    else:
        cnt += r[c]
        c += 1
print(cnt)
