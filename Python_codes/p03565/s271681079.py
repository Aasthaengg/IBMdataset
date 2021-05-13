S=input()
T=input()
tmp=[]
for i in range(len(S)):
    flag=True
    for j in range(min(len(T),len(S)-i)):
        if S[i+j]==T[j] or S[i+j]=="?" or T[j]=="?":
            continue
        else:
            flag=False
    if flag:
        rec=S[:i]+T+S[i+len(T):]
        if len(rec)==len(S):
            rec=rec.replace("?","a")
            tmp.append(rec)
if tmp==[]:
    print("UNRESTORABLE")
    exit()
tmp.sort()
print(tmp[0])