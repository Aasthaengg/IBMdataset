s=input()
n=len(s)
if(s==s[::-1]):
    if((s[:(n-1)//2]==s[:(n-1)//2][::-1]) and (s[(n+4)//2-1:]==s[(n+4)//2-1:][::-1])):
        print('Yes')
    else:
        print('No')
else:
    print("No")