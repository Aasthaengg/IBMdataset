S=input()
a=[0]*7
a[0]=int(S[0])
a[2]=int(S[1])
a[4]=int(S[2])
a[6]=int(S[3])
for i in range(2**3):
    j=bin(int(i))[2:]
    while len(j)<3:
        j="0"+j
    for k in range(3):
        if j[k]=="0":
            a[2*k+1]="+"
        else:
            a[2*k+1]="-"
    ans=a[0]
    if a[1]=="+":
        ans+=a[2]
    else:
        ans-=a[2]
    if a[3]=="+":
        ans+=a[4]
    else:
        ans-=a[4]
    if a[5]=="+":
        ans+=a[6]
    else:
        ans-=a[6]
    if ans==7:
        print(S[0]+a[1]+S[1]+a[3]+S[2]+a[5]+S[3]+"=7")
        break
