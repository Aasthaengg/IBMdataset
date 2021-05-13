N = int(input())
pre = None
is_inc = None
ans = 1
for num in list(map(int, input().split())):
    if pre is None:
        pre = num
        continue

    if is_inc is None and num > pre:
        is_inc = True
    elif is_inc is None and num < pre:
        is_inc = False
    elif (is_inc and num < pre) or (not is_inc and num > pre):
        ans += 1
        is_inc = None

    pre = num

print(ans)
