n,m = map(int, input().split())
A = sorted(list(map(int, input().split())))[::-1]

x = 1/(4*m) * sum(A)
cnt = 0
for a in A:
    if a >= x: cnt += 1
    else: break
print("Yes" if cnt >= m else "No")