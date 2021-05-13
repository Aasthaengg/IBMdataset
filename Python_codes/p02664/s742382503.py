t=input()
s=[0]*len(t)

for i in range(len(t)):
  
    if t[i]=='?':
        if i==0:
            if len(t)>=2:
                if t[i+1]=='D':
                    s[i]='P'
                else:
                    s[i]='D'
            else:s[i]='D'
      
      
        elif i==len(t)-1:
            s[i]='D'
        
    
        else:
            if s[i-1]=='P':s[i]='D'
            elif t[i+1]=='P':s[i]='D'
            else:s[i]='P'

    elif t[i]=='D' or t[i]=='P':s[i]=t[i]
    else:continue
#print(s)
print(''.join(s))