n = int(input())
a = [int(i) for i in input().split()]
a.sort()
a_left, a_right = a[0], a.pop()
ans_list = []
for i in range(1, n - 1):
    ans_list.append([[a_right, a_left][a[i] >= 0], a[i]])
    a_right, a_left = a_right - [a[i], 0][a[i] >= 0], a_left - [0, a[i]][a[i] >= 0]
ans_list.append([a_right, a_left])
print(a_right - a_left)
[print(*ans_list[i]) for i in range(n-1)]