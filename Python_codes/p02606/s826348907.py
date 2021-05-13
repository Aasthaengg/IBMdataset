L, R, D = map(int, input().split())

first = L + (D - (L % D)) % D
last = R - (R % D)
ans = 0
if L <= first <= R and L <= last <= R:
    ans = (last - first) // D + 1

print(ans)

