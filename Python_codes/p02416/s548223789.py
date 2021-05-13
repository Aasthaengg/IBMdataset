while True:
    num = input()
    if num[0] == '0':
        break
    print(sum(map(int, num)))