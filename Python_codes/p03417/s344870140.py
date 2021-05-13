n, m = map(int, input().split())
if n == 1 and m == 1:
    ans = 1
elif n == 1 and m != 1:
    ans = m-2
elif n != 1 and m == 1:
    ans = n-2
else:
    ans = n * m
    ans -= 2*n
    ans -= 2*m
    ans += 4
print(ans)