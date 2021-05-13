n, a, b = map(int, input().split())

if(n >= a+b):
    print(min(a, b), end=' ')
    print(0)
else:
    print(min(a, b), end=' ')
    print(a+b-n)