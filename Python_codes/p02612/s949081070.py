n=int(input())

if n%1000 == 0:
    print(0)
else:
    c = n%1000
    print(1000-c)