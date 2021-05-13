import itertools

n = int(input())
a_list = list(map(int, input().split()))

xn = sum(a_list) // 2 - sum(a_list[:n-1:2])
x = a_list[-1] - xn
for a in a_list:
    print(x * 2)
    x = a - x