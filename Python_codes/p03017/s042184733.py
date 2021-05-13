n,a,b,c,d=map(int,input().split())
s=[0]+list(input())
if c<d:
    for i in range(a,d):
        if s[i]==s[i+1]=="#":
            print("No")
            break
    else:
        print("Yes")
else:
    for j in range(a,c):
        if s[j]==s[j+1]=="#":
            print("No")
            break
    else:
        for k in range(b-1,d):
            if s[k]==s[k+1]==s[k+2]==".":
                    print("Yes")
                    break
        else:
            print("No")