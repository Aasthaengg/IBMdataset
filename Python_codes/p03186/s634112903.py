a, b, c = map(int, input().split())

if b >= c-1 or a  + b >= c-1:
    print(b + c)
else:
    print(min(2*(a+b) + 1 - a , b+c))


