a_list = list(map(int,input().split()))
a_list.sort()
print(a_list[2]-a_list[1] + a_list[1] - a_list[0])