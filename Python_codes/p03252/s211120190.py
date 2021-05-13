S=input()
T=input()

flg=True

def dic(DIC,str):
    for num in range(len(str)):
        if str[num] not in DIC:
            DIC[str[num]]=[num]
        else:
            DIC[str[num]].append(num)
    return DIC

D_S={}
D_T={}

D_S=dic(D_S,S)
D_T=dic(D_T,T)

if len(D_S)==len(D_T):
    for lst in D_S.values():
        if lst not in D_T.values():
            flg=False
else:
    flg=False

if flg==True:
    print("Yes")
else:
    print("No")