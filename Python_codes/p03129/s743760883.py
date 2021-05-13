n, k = map(int, input().split())

w_n = 0
if n % 2 == 0:
    w_n = n
else:
    w_n = n + 1

if (w_n / 2) >= k:
    print("YES")
else:
    print("NO")