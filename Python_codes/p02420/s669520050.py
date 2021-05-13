while True:
    s = input()
    if s == '-': break
    cnt = int(input())
    for x in range(0, cnt):
        shufint = int(input())
        s = s[shufint:] + s[:shufint]
    print(s)

