n=int(input())
s=str(input())
if(n%2!=0):
    print('No')
else:
    if(s[0:len(s)//2]==s[len(s)//2:]):
        print('Yes')
    else:
        print('No')