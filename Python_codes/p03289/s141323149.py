#n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
s=list(input())
chk=list("abcdefghijklmnopqrstuvwxyz")
flag="WA"
n=len(s)

if s[0]=="A":
    temp=s[2:n-1]
    if temp.count("C")==1:
        ind=temp.index("C")
        ind+=2
        del s[0]
        del s[ind-1]
        for st in s :
            if st in chk:
                pass
            else:
                flag="WA"
                break
            flag="AC"
print(flag)
