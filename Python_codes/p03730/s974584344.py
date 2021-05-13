A, B, C = list(map(int, input().split()))
rs = []
flag = 0

for i in range(1, int(1e20)):
    r = A * i % B
    if r == C:
        flag = 1
        break
    if r in rs:
        break
    rs.append(r)

ans = 'YES' if flag else 'NO'
print(ans)