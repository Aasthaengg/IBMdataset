N, K = map(int, input().split())
A = [int(i) for i in input().split()]
BC = [0 for _ in range(40)]
for a in A:
    for i, b in enumerate(bin(a)[2:].zfill(40)):
        if b == '0':
            BC[i] += 1
# print(BC)

ans = 0
for i in range(40):
    if BC[i] > N//2 and K >= 2**(39-i):
        K -= 2**(39-i)
        ans += 2**(39-i)*BC[i]
    else:
        ans += 2**(39-i)*(N-BC[i])
print(ans)
