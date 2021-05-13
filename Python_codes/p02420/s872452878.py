while True:
    tmp=input()
    if tmp=="-":
        break
    else:
        s=tmp
        n=int(input())
        for _ in range(n):
            h=int(input())
            s=s[h:]+s[:h]
        print(s)


