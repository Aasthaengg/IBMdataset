while True:
    s = input()
    if s == '-':
        break
    else:
        num = int(input())
        for i in range(num): 
            t = int(input())
            s = s[t:] + s[:t]
        print(s)
