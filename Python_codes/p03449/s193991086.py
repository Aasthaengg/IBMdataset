N = int(input())
x = list(map(int, input().split(' ')))
y = list(map(int, input().split(' ')))

def down_count():
    count = x[0]
    for i in range(N):
        count += y[i]
    return count

x_list = []

def switch_count():
    for i in range(N - 1):
        sums = x_list[i] + x[i + 1] - y[i]
        x_list.append(sums)

down_sum = down_count()
x_list.append(down_sum)
switch_count()
x_list.sort(reverse=True)
print(x_list[0])