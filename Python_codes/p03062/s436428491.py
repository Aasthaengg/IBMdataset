n = int(input())
a = list(map(int,input().split()))
a_abs = [0]*n
is_minus = [0]*n

for i in range(n):
    if a[i] >= 0:
        a_abs[i] = a[i]
    else:
        a_abs[i] = -1 * a[i]
        is_minus[i] = 1

a_abs.sort()
if sum(is_minus) % 2 == 0:
    ans = sum(a_abs)
else:
    ans = sum(a_abs) - 2*a_abs[0]

print(ans)