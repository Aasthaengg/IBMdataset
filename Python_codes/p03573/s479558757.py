abc = list(map(int, input().split()))

abc.sort()
if abc[0] == abc[1]:
    print(abc[2])
else:
    print(abc[0])