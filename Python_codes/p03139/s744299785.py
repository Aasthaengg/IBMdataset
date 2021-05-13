n, a, b=map(int, input().split())
if n>(a+b):
    print("{} {}".format(min([a,b]), 0))
else:
    print("{} {}".format(min([a,b]), abs(n-(a+b))))
