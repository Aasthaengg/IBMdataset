s=input()
i=0
flag=0
while i<len(s):
    if (i+1)%2==0:
        if s[i] =="L" or s[i] =="U" or s[i] =="D":
            pass
        else:
            flag+=1
         
    else:
        if s[i] =="R" or s[i] =="U" or s[i] =="D":
            pass
        else:
            flag+=1
     

    if flag==1:
        break


    i+=1

if flag==1:
    print("No")
else:
    print("Yes")