x = list(map(int, input().split()))

for i in x:
    if i == 0:
        print(x.index(i) + 1)