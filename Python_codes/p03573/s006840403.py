a_list = list(map(int, input().split()))

for i in a_list:
    if a_list.count(i) == 2:
        pass
    else:
        print(i)