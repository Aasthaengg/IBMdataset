a, b = map(int, input().split())
if a >= b + 1:
    print(a + a-1)
if b >= a+1:
    print(b + b-1)
if a == b:
    print(a+a)