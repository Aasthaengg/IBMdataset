S=input()[::-1]
N=len(S)
T=['maerd','esare','resare','remaerd']
ans='YES'
i=0
while i<N:
    if S[i:i+5]==T[0]:
        i+=5
    elif S[i:i+5]==T[1]:
        i+=5
    elif S[i:i+6]==T[2]:
        i+=6
    elif S[i:i+7]==T[3]:
        i+=7
    else:
        ans='NO'
        break
print(ans)