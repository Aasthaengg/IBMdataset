lst = input().split()

if lst[0] == lst[1]:
    print(lst[2])
elif lst[1] == lst[2]:
    print(lst[0])
elif lst[2] == lst[0]:
    print(lst[1])
