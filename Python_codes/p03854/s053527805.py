S=input()
i=len(S)
isOK=True
while len(S[0:i])>0:
    if len(S[0:i])<5:
        isOK=False
        break

    if len(S[0:i])>=7:
        st=S[i-7:i]
        if st=="dreamer":
            i=i-7
            continue
    
    if len(S[0:i])>=6:
        st=S[i-6:i]
        if st=="eraser":
            i=i-6
            continue
    if len(S[0:i])>=5:
        st=S[i-5:i]
        if st=="erase" or st=="dream":
            i=i-5
            continue
        else:
            isOK=False
            break


if isOK:
    print("YES")
else:
    print("NO")
