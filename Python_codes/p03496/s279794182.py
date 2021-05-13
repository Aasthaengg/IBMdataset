n = int(input())
a = list(map(int, input().split()))
mn = min(a)
mx = max(a)
bb = mx if abs(mx) >= abs(mn) else mn
base = a.index(bb)
print(n + n - 1)
[print(base+1, i+1) for i in range(n)]
if abs(mx) >= abs(mn):
    [print(i, i+1) for i in range(1,n)]
else:
    [print(i+1, i) for i in range(1,n)[::-1]]
