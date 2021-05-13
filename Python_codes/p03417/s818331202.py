n, m = map(int, input().split())
min_value = min(n, m)
max_value = max(n, m)
ans = 0
if min_value == 1:
    if max_value == 1:
        ans = 1
    elif max_value == 2:
        ans = 0
    else:
        ans = max_value - 2
elif min_value == 2:
    ans = 0
else:
    ans = (min_value-2)*(max_value-2)

print(ans)