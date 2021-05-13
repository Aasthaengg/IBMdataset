int_s = list(map(int, input().split()))

for int_ in int_s:
    if int_s.count(int_) == 1:
        print(int_)
        break