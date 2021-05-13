n = [x for x in input().split()]
for i in n:
    if n.count(i) == 1:
        print(i)
        break