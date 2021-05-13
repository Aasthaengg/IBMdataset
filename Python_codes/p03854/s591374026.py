s=input()
while 1:
    n = len(s)
    if n==0:
        print("YES")
        exit()
    elif 1<=n<=4:
        print("NO")
        exit()
    else:
        if s[n-5:n]=="dream" or s[n-5:n]=="erase":
            s=s[:n-5]
        elif s[n-6:n]=="eraser":
            s=s[:n-6]
        elif s[n-7:n]=="dreamer":
            s=s[:n-7]
        else:
            print("NO")
            exit()