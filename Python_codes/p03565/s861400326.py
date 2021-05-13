S=input()
T=input()

def isOK(s):
    res=[]
    if len(s)<len(T):
        return res
    for i in range(len(s)-len(T)+1):
        ns=s[i:i+len(T)]
        for j in range(len(T)):
            if ns[j]!='?' and not ns[j]==T[j]:
                break
        else:
            res.append(s[:i]+T+s[i+len(T):])
    return res

OK_list=isOK(S)
if OK_list:
    OK_list.sort()
    print(OK_list[0].replace('?','a'))
else:
    print('UNRESTORABLE')