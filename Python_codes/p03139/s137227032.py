n, a, b = [int(i) for i in input().split()]
if n-(a+b)>0:
    print(min(a,b), 0)
else:
    print(min(a,b), abs(n-(a+b)))