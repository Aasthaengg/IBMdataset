n = int(input())
a = [int(i) for i in input().split()]
ans = 0
a.sort()
a_left, a_right = a[0], a.pop()
minus, plus = [], []
for i in range(1, n - 1):
    if a[i] < 0:
        minus.append(a[i])
    else:
        plus.append(a[i])

ans_list = []
for i in range(len(minus)):
    ans_list.append([a_right ,minus[i]])
    a_right -= minus[i]
for i in range(len(plus)):
    ans_list.append([a_left ,plus[i]])
    a_left -= plus[i]
ans_list.append([a_right, a_left])

print(a_right - a_left)
[print(*ans_list[i]) for i in range(n-1)]