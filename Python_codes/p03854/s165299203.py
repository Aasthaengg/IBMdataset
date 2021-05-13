s=input()
rev=s[::-1]
can='YES'
while(len(rev)!=0):
    if(rev[:3]=='rem'):
        if(rev[:7]=='remaerd'):
            rev=rev[7:]

        else:
            can='NO'
            break
    
    elif(rev[:3]=='res'):
        if(rev[:6]=='resare'):
            rev=rev[6:]

        else:
            can='NO'
            break
    
    elif(rev[0]=='e'):
        if(rev[:5]=='esare'):
            rev=rev[5:]

        else:
            can='NO'
            break
    elif(rev[0]=='m'):
        if(rev[:5]=='maerd'):
            rev=rev[5:]

        else:
            can='NO'
            break
    else:
        can='NO'
        break

print(can)