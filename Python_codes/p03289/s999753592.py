s = input()
flg = 0
k = 0
if s[0] == "A":
    for i in range(1, len(s)):
        if s[i] == "C" and i != 1 and i != len(s) -1:
            if flg == 0:
                flg = 1
                k = i
            else:
                print("WA")
                exit()
    if k == 0:
        print("WA")
        exit()
    else:
        for j in range(1, len(s)):
            if s[j].isupper():
                if j != k:
                    print("WA")
                    exit()
            else:
                continue
else:
    print("WA")
    exit()
    
print("AC" if flg == 1 else "WA")