while(True):
    s = input()
    if(s == '-'): break
    n = int(input())
    for _ in range(n):
        tmp = int(input())
        s = s[tmp:] + s[:tmp]
    print(s)