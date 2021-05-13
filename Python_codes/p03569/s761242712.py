s=input()

ll=0
rr=len(s)-1

cnt=0
while ll<=rr:
    if s[ll]==s[rr]:
        ll+=1
        rr-=1
    elif s[ll]=="x":
        cnt+=1
        ll+=1
    elif s[rr]=="x":
        cnt+=1
        rr-=1
    else:
        print(-1)
        exit()
print(cnt)

