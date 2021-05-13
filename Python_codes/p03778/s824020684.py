w, a, b = [int(i) for i in input().split()]
if a - b <= 0:
    ans = b - (a+w)
else:
    ans = a - (b+w)

print(ans if ans > 0 else 0)