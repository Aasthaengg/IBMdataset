x = int(input())
n = x%100

if n%5:
    if 100*(n//5+1) <= x-n:
        print(1)
    else:
        print(0)
else:
    if 100*(n//5) <= x-n:
        print(1)
    else:
        print(0)
