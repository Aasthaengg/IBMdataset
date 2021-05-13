s=input()
if len(s)==7:
    if s=="keyence":
        print("YES")
    else:
        print("NO")
else:
    if s[:7]=="keyence":
        print("YES")
    elif s[-7:]=="keyence":
        print("YES")
    else:
        for i in range(7-1):
            if s[:i+1]+s[-(7-i-1):]=="keyence":
                print("YES")
                exit()
        print("NO")