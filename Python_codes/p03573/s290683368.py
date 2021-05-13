As = list(map(int, input().split()))
for a in As:
    if As.count(a) == 1:
        print(a)
        exit()