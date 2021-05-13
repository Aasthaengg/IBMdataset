import itertools
x = int(input())

if x >= 2600:
    print(1)
    exit()

cnt = 0
for i in range(0, 25):
    for v in itertools.combinations_with_replacement([100, 101, 102, 103, 104, 105], i):
        if sum(v) == x:
            print(1)
            exit()
print(0)