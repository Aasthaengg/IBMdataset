while True:
    s = input()
    if s == '-':
        break
    for i in (int(input()) for i in range(int(input()))):
        s = s[i:] + s[:i]
    print(s)