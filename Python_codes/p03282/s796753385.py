s=input()
k=int(input())
if s[0]!="1":
    print(s[0])
else:
    cnt=0
    for i in range(len(s)):
        if s[i]=="1":
            cnt+=1
        else:
            break
    if cnt>=k:
        print(1)
    else:
        print(s[cnt])