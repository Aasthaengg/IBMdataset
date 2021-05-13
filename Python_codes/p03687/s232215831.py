alphabetlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

s=input()
for i in range(1,len(s)):
    if s[i]!=s[0]:
        break
else:
    print(0)
    exit()

ans=100
for moji in alphabetlist:
    count=0
    test=s
    while test:
        new=""
        flag=True
        for i in range(0,len(test)-1):
            if test[i]!=moji and test[i+1]!=moji:
                new+=test[i]
                flag=False
            else:
                new+=moji
        count+=1
        test=new
        if flag:
            break
    ans=min(ans,count)

print(ans)
