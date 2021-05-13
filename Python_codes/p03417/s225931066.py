a,b=map(int, input().split())

if a == 1 and b == 1:
    print(1)
if a == 1 and b != 1:
    print(b-2)
if a != 1 and b == 1:
    print(a-2)
if a != 1 and b != 1:
    print(a*b-2*(a+b)+4)