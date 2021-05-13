s=input()

alps="abcdefghijklmnopqrstuvwxyz"
if len(s)==26:
    if s=="zyxwvutsrqponmlkjihgfedcba":
        print(-1)
    else:
        dels=[]
        for i in range(26):
            dels.append(s[25-i])
            for del_i in dels:
                if s<s[:25-i]+del_i:
                    print(s[:25-i]+del_i)
                    exit()
else:
    for alp in alps:
        if s.count(alp)==0:
            print(s+alp)
            exit()
