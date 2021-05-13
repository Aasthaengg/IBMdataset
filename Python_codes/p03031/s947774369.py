n, m = map(int, input().split())
denq = []
for _ in range(m):
    ks = tuple(map(lambda x: int(x)-1, input().split()))
    denq.append(ks[1:])
P = tuple(map(int, input().split()))

ans = 0
for i in range(2**n):
    switch_states = [(i>>j)&1 for j in range(n)]
    for idq, dq in enumerate(denq):
        counts = 0
        for s in dq:
            counts += switch_states[s]
        if counts%2 != P[idq]:
            break
    else:
        ans += 1
print(ans)
