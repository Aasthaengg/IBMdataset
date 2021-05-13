s=input()

ans=0
while s!="":
    
    if s[-6:] =="eraser":
        s=s[:-6]
        
    elif s[-5:]=="dream":
        s=s[:-5]
        
    elif s[-7:]=="dreamer":
        s=s[:-7]
        
    elif s[-5:]=="erase":
        s=s[:-5]
        
    else:
        ans=1
        print("NO")
        break

if ans==0:
    print("YES")
