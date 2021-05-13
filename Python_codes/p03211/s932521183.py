def resolve():
    s = input()
    a = 753
    for i in range(len(s)-2):
        b = abs(int(s[i:i+3]) - 753)
        if b < a:
            a = b
    print(a)
resolve()    