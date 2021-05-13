n, m = map(int, input().split())

if m <= 2*n:
    ans = int(m//2)
else:
    res_c = m - 2*n
    ans = n + int(res_c//4)

print(ans)