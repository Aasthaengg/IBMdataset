n, a, b = map(int, input().split())
min_ = (n-1)*a+b
max_ = a+(n-1)*b
if max_ < min_:
    print(0)
    exit()
print(max_-min_+1)
