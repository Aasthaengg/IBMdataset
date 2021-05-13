s=input(); n=len(s)
if s=="zyxwvutsrqponmlkjihgfedcba":
    print(-1);exit()
if len(s)!=26:
    for c in range(ord("a"),ord("z")+1):
        c=chr(c)
        if not (c in s):
            print(s+c);exit()

now="zz"
for i in range(n-1,-1,-1):
    if s[i-1]<s[i]:
        if i==1:
            print(chr(ord(s[0])+1));exit()
        qq=s[i]
        for nowc in s[i+1:]:
            if nowc> s[i-1] and qq>nowc:
                qq=nowc
        print(s[:i-1]+qq);exit()