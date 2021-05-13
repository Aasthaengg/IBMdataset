a, b, c = map(int, input().split())

i = 0
while True:
    if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
        print(i)
        break
    elif a == b == c:
        print(-1)
        break
    a_h = a / 2
    b_h = b / 2
    c_h = c / 2
    a = b_h + c_h
    b = a_h + c_h
    c = a_h + b_h
    i += 1