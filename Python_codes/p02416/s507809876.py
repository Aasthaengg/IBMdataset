while True:
    s = input()
    if s == '0':
        break
    print(sum(list(map(int, list(s)))))