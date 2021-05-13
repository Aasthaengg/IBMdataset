s=input()
if s[0]!="A":
    print("WA")
else:
    cnt=0
    for i in range(min(2,len(s)-2),max(2,len(s)-2)+1):
        if s[i]=="C":
            cnt+=1
    if cnt!=1:
        print("WA")
    else:
        for i in range(1,len(s)):
            if s[i]!="C":
                if ord("a")>ord(s[i]) or ord("z")<ord(s[i]):
                    print("WA")
                    break
        else:
            print("AC")