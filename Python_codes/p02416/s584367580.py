while True:
    s = input()
    if s == '0':
        break
    SUM = 0
    for i in s:
        SUM += int(i)
    print(SUM)

