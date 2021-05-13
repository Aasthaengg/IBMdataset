A=int(input())
print(0)
S=input()
if S=="Vacant":
    exit()

MAX=A
MIN=0
MID=(MAX+MIN)//2
for i in range(19):
    print(MID)
    s=input()
    if s=="Vacant":
        exit()
    elif MID%2==0:
        if S==s:
            MIN=MID
            MID=(MAX+MIN)//2
        else:
            MAX=MID
            MID=(MAX+MIN)//2
    else:
        if S!=s:
            MIN=MID
            MID=(MAX+MIN)//2
        else:
            MAX=MID
            MID=(MAX+MIN)//2