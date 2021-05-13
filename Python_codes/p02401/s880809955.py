while True:
    s = raw_input().split()
    if s[1] == '?':
        break
    elif s[1]=='+':
        print (int(s[0])+int(s[2])) 
    elif s[1]=='-':
        print (int(s[0])-int(s[2])) 
    elif s[1]=='*':
        print (int(s[0])*int(s[2])) 
    elif s[1]=='/':
        print (int(s[0])/int(s[2])) 