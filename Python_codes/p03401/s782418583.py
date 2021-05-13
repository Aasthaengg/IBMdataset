n = int(input())
a_list = [0] + [int(x) for x in input().split()] + [0]
d1_list = [abs(a_list[i + 1] - a_list[i]) for i in range(n + 1)]
d2_list = [abs(a_list[i + 2] - a_list[i]) for i in range(n)]
travel_all = sum(d1_list)
for i in range(n):
    print(travel_all - d1_list[i] - d1_list[i + 1] + d2_list[i])