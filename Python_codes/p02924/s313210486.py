n = int(input())
d,m = divmod(n,2)
if m != 0:
    print(n*d)

else:
    print(n*(d - 1) + d)