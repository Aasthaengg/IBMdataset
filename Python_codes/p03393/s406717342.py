s=input()
if s=="zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()
x=len(s)

al=[0]*26

if x!=26:
    for i in s:
        al[ord(i)-97]=1
    
    for i in range(26):
        if al[i]==0:
            s+=chr(97+i)
            print(s)
            exit()

else:
    option=[]
    
    for i in reversed(range(26)):
        option=sorted(option)
        num=ord(s[i])
        if i==25:
            option.append(num)
        else:
            if num>max(option):
                option.append(num)
            else:
                s=s[:26-len(option)-1]
                for i in option:
                    if i>num:
                        s+=chr(i)
                        print(s)
                        exit() 
