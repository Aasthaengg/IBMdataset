N, K = map(int, input().split())
*A, = map(int, input().split())

target = []
while K:
    target.append(K%2)
    K//=2
target.extend([0]*(50-len(target)))

b = [0]*50
for i in A:
    p = 0
    while i:
        b[p] += i%2
        i //=2
        p += 1

target.reverse()
b.reverse()

c = [0]*50
for i in range(50):
    e, f = b[i], N-b[i]
    if e==f:
        c[i] = 0
    elif e>f:
        c[i] = 0
    else:            
        c[i] = 1

ans = 0
for i in range(50):
    if target[i]:
        o = []
        for j in range(i):
            o.append(target[j])
        o.append(0)
        for j in range(i+1, 50):
            o.append(c[j])
        v = 0
        for j in range(50):
            if o[j]:
                v += (2**(50-j-1))*(N-b[j])
            else:
                v += (2**(50-j-1))*b[j]
        ans = max(ans, v)

v = 0
for j in range(50):
    if target[j]:
        v += (2**(50-j-1))*(N-b[j])
    else:
        v += (2**(50-j-1))*b[j]
ans = max(ans, v)

print(ans)