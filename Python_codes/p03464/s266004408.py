k = int(input())
a = tuple(map(int, input().split()))

l, r = 2, 2
ans = (-1,)
for x in reversed(a):
    l = ((l + x - 1) // x) * x
    # print(x, l, r)
    if r < l:
        break
    r = ((r // x) * x) + (x - 1)
else:
    ans = (l, r)
print(*ans)
