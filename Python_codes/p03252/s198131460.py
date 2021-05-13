S=list(input())
T=list(input())
slist=[None]*26
flag=True
for i in range(len(S)):
    if slist[ord(S[i])-97] == None and T[i] not in slist:
        slist[ord(S[i])-97] = T[i]
    elif slist[ord(S[i])-97] != T[i]:
        flag = False
        break
    else:
        slist[ord(S[i])-97] = T[i]


if flag:
    print("Yes")
else:
    print("No")
    

