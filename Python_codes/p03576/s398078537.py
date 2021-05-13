N, K = map(int, input().split())
x_list = [0]*N
y_list = [0]*N
for i in range(N):
    x_list[i], y_list[i] = map(int, input().split())

x_sort_list = sorted(x_list)
y_sort_list = sorted(y_list)
ans = float("inf")

for i in range(len(x_sort_list)):
    for j in range(len(y_sort_list)):
        for k in range(i+1, len(x_sort_list)):
            for l in range(j+1, len(y_sort_list)):
                num = 0
                for m in range(N):
                    if x_sort_list[i] <= x_list[m] <= x_sort_list[k] and y_sort_list[j] <= y_list[m] <= y_sort_list[l]:
                        num += 1
                if num >= K:
                    ans = min((x_sort_list[k] - x_sort_list[i]) * (y_sort_list[l] - y_sort_list[j]), ans)

print(ans)
