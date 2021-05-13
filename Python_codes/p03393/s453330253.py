s=input()
if len(s)<26:
    num=list(range(97,123))
    for i in range(len(s)):
        num.remove(ord(s[i]))
    print(s+chr(num[0]))
else:
    if s=="zyxwvutsrqponmlkjihgfedcba":
        print(-1)
    else:
        for i in range(25):
            if ord(s[-1-i])>ord(s[-2-i]):
                str1=s[-2-i]
                num1=26-(2+i)
                break
        ans=123
        num3=ord(str1)
        for i in range(num1+1,26):
            num4=ord(s[i])
            if num3<num4:
                ans=min(ans,num4)
        print(s[:num1]+chr(ans))
