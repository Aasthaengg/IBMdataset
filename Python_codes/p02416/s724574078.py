while True:
    x = str(input())
    if x == '0':
        break
    num = list(x)
    num2 = list(map(int, num))
    print(sum(num2))
