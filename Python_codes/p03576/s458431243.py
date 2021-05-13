import sys
import heapq
INF = 1e20
n, k = [int(i) for i in sys.stdin.readline().split()]
ls = []
for i in range(n):
    x, y = [int(i) for i in sys.stdin.readline().split()]
    ls.append((x, y))
ls.sort(key=lambda x:x[0])
x_ls, y_ls = zip(*ls)
best = INF

x_ls = sorted(list(x_ls))
y_ls = sorted(list(y_ls))
for left_ind in range(n - k + 1):
    left = x_ls[left_ind]
    for right_ind in range(left_ind + k - 1, n):
        right = x_ls[right_ind]
        for down_ind in range(n - k + 1):
            down = y_ls[down_ind]
            for up_ind in range(down_ind + k - 1, n):
                up = y_ls[up_ind]
                cnt = 0
                for i in range(n):
                    x, y = ls[i]
                    if left <= x <= right and up >= y >= down:
                        cnt += 1
                if cnt >= k:
                    best = min(best, (up - down) * (right - left))
print(max(1,best))