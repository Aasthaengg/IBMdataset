N , K = [int(x) for x in input().split()]
A = [0] + [int(x) for x in input().split()]

orb = [1]
counter = [-1] * (N + 1)
v = A[1]
counter[1] = 0
c = 0
while 1:
    c += 1
    if counter[v] == -1:
        counter[v] = c
        orb.append(v)
        v = A[v]
    else:
        break

L = c - counter[v]
T = counter[v]

if K < c:
    ans = orb[K]
else:
    ans = orb[(K - T) % L + T]

print(ans)