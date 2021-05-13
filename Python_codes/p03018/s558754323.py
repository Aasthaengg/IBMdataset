S=input()
#ABCBCBC
N=len(S)
if N<3:
    print(0)
    exit()
S=list(S)
#abc前にaが続く数
As=0
#abcごにbc続く数
BCs=0
ans=0
flag=False
safe=-1
for i in range(N-2):
    if "".join(S[i:i+3])=="ABC":
        ans+=1
        ans+=As


        S[i]="B"
        S[i+1]="C"
        S[i+2]="A"
        safe=i+1

    elif S[i]=="A":
        As+=1
    else:
        if i!=safe:
            As=0
    #print(As)

print(ans)