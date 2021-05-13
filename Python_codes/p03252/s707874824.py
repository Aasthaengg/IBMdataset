S = input()
T = input()
dic1={}
dic2={}
for i in range(len(S)):
    s = S[i]
    t = T[i]
    if s!=t:
        if (s not in dic1) and (t not in dic2):
            dic1[s]=t
            dic2[t]=s
        elif (s in dic1) and (t in dic2):
            if dic1[s]!=t:
                print('No')
                break
            else:
                continue
        else:
            print('No')
            break
    else:
        dic1[s]=t
        dic2[t]=s
else:
    print('Yes')