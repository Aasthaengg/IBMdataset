h = int(input())
w = int(input())
n = int(input())

if h < w:
    if n % w == 0:
        print(n // w)
    else:
        print(n // w + 1)
else:
    if n % h == 0: 
        print(n // h)
    else:
        print(n // h + 1)