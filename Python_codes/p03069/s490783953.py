N=int(input())
S=input()
flag="-1"
l=[]
b=0
w=0
for i in range(N):
    if S[i]=="#":
        if flag=="w":
            l.append([b,w])
            b=1
            w=0
            flag="b"
        else:
            flag="b"
            b+=1
    else:
        if flag=="b":
            w+=1
            flag="w"
        elif flag=="-1":
            continue
        else:
            flag="w"
            w+=1
if flag=="w":
    l.append([b,w])

aw=0
ab=0
for i in range(len(l)):
    aw+=l[i][0]
    ab+=l[i][1]
ans=[]
ans.append(aw)
ans.append(ab)
tmpw=0
tmpb=0
val=0
for i in range(len(l)):
    tmpw+=l[i][1]
    tmpb+=l[i][0]
    val=(ab-tmpw)+tmpb
    ans.append(val)
print(min(ans))