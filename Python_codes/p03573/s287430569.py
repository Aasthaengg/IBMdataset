_list = input().split()
for i in _list:
    if _list.count(i) == 1:
        print(i)
        exit
