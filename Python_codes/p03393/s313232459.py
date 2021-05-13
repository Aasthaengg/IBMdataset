s=input()
a=97
if s=="zyxwvutsrqponmlkjihgfedcba":
    print("-1")
elif len(s)!=26:
    for i in range(26):
        if chr(a+i) not in s:
            print(s+chr(a+i))
            exit()
else:
    for i in range(26):
        for j in range(i+1):
            if s[-(i+1)]<s[-(j+1)]:
                print(s[:-(i+1)]+s[-(j+1)])
                exit()