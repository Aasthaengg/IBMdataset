s = list(input())
flag = 1
if s[0] == "A" :
    if s[2:-1].count("C") == 1 :
        for i in range(1,len(s)) :
            if i != s[2:-1].index("C") + 2 :
                if s[i] != s[i].lower() :
                    flag = 0
                    break
    else :
        flag = 0
else :
    flag = 0

print("AC" if flag ==1 else "WA")
