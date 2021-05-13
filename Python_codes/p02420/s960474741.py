while True:
    s = input()
    if s == "-":
        break
    for i in range(int(input())):
        shuf = int(input())
        s = s[shuf:] + s[:shuf]
    print(s)