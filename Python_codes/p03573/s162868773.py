abc = [int(i) for i in input().split()]
if abc[0] == abc[1]:
    print(abc[2])
else:
    print((set(abc[:2]) - (set(abc[:2]) & set([abc[2]]))).pop())