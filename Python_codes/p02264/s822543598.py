n, q = [int(e) for e in input().split()]
A = []
res = []
for i in range(n):
    l = input().split()
    A.append((l[0], int(l[1])))

idx = 0
tot_t = 0
while A:
    dif = A[0][1] - q
    if dif <= 0:
        tot_t += A[0][1]
        res.append((A[0][0], tot_t))
        A.pop(0)
    else:
        tmp = (A[0][0], dif)
        A.pop(0)
        A.append(tmp)
        tot_t += q

for e in res:
    print(e[0], e[1])

