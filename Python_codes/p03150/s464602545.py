s=input()
if s[-7]+s[-6]+s[-5]+s[-4]+s[-3]+s[-2]+s[-1]=='keyence':
    print("YES")
    exit()
elif s[0]=='k':
    if s[-6]+s[-5]+s[-4]+s[-3]+s[-2]+s[-1]=='eyence':
        print("YES")
        exit()
    elif s[1]=='e':
        if s[-5]+s[-4]+s[-3]+s[-2]+s[-1]=='yence':
            print("YES")
            exit()
        elif s[2]=='y':
            if s[-4]+s[-3]+s[-2]+s[-1]=='ence':
                print("YES")
                exit()
            elif s[3]=='e':
                if s[-3]+s[-2]+s[-1]=='nce':
                    print("YES")
                    exit()
                elif s[4]=='n':
                    if s[-2]+s[-1]=='ce':
                        print("YES")
                        exit()
                    elif s[5]=='c':
                        if s[-1]=='e':
                            print("YES")
                            exit()
print("NO")