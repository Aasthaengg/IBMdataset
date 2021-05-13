S=input()
N=len(S)

idx=N-1
ans="YES"
while idx>=0:
    now=S[idx]
    if now=="m":
        if S[idx-4:idx+1]!="dream":
            ans="NO"
            break
        else:idx-=5
    elif now=="e":
        if S[idx-4:idx+1]!="erase":
            ans="NO"
            break
        else:idx-=5
    elif now=="r":
        if S[idx-5:idx+1]=="eraser":
            idx-=6
        elif S[idx-6:idx+1]=="dreamer":
            idx-=7
        else:
            ans="NO"
            break
print(ans)