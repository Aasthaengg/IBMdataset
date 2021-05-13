s = list(input())
c0 = s.count("0")
c1 = s.count("1")
if c0 >= c1:
    print(2*c1)
else:
    print(2*c0)