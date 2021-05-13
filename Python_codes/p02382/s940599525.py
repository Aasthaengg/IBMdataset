num = int(input())
x_list = [float(i) for i in input().split()]
y_list = [float(i) for i in input().split()]
distance = 0
tmp = 0
sum_dis = 0
for i in range(1, 4):
    for j in range(num):
        tmp = (abs(x_list[j] - y_list[j])) ** i
        distance += tmp
        if sum_dis < tmp and i == 1:
            sum_dis = tmp
    distance = distance ** (1/i)
    print("{:.6f}".format(distance))
    distance = 0
print("{:.6f}".format(sum_dis))