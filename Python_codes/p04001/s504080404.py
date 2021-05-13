S=list(input())
ans=0
for i in range(2**(len(S)-1)):
    kari=[""]*(len(S)-1)
    for j in range(len(S)-1):
        if ((i>>j)&1):
            kari[j]="+"
    hako=[]
    kasu=0
    gomi=0
    for j in range(len(kari)+len(S)):
        if j%2==0:
            hako.append(S[kasu])
            kasu+=1
        else:
            hako.append(kari[gomi])
            gomi+=1
    #print(hako)
    hako="".join(hako)
    #hako=hako.replace(",","")
    #print(hako)
    ans+=eval(hako)
print(ans)