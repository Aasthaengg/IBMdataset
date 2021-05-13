a,b,c = [int(x) for x in input().split()]
if c-1 <= a+b:
    print(c+b)
else:
    print(b+a+b+1)