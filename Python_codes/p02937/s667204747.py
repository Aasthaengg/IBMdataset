alphabetlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
S=input()
T=input()
Sdata=[[] for i in range(26)]
for i in range(0,len(S)):
    Sdata[alphabetlist.index(S[i])].append(i)
ans=0
for i in range(len(T)):
    if Sdata[alphabetlist.index(T[i])]==[]:
        ans=-1
if ans!=-1:
    sequence=0
    number=-1
    for i in range(0,len(T)):
        x=T[i]
        n=alphabetlist.index(x)
        start=0
        end=len(Sdata[n])-1
        while end-start>1:
            test=(end+start)//2
            if Sdata[n][test]>number:
                end=test
            else:
                start=test
        if Sdata[n][start]>number:
            number=Sdata[n][start]
        elif Sdata[n][end]>number:
            number=Sdata[n][end]
        else:
            sequence+=1
            number=Sdata[n][0]
    ans=sequence*len(S)+number+1
print(ans)