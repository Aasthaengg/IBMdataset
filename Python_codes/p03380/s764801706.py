from bisect import bisect_left
n = int(input())
a_list = sorted([int(x) for x in input().split()])
base = a_list[-1] / 2
i = bisect_left(a_list, base)
if i > 0:
    i -= 1
ans = [a_list[-1], a_list[i], abs(a_list[i] - base)]
for i in range(i + 1, n):
    temp = abs(a_list[i] - base)
    if temp >= ans[2]:
        break
    ans[1] = a_list[i]
    ans[2] = temp
print(ans[0], ans[1])