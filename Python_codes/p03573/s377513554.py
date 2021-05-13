ABC = list(map(int, input().split()))
for t in ABC:
    if ABC.count(t) == 1:
        print(t)