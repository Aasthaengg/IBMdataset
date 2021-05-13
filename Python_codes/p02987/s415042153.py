import collections
S=input()
s=collections.Counter(S)
S=list(set(S))
if len(S)!=2:
    print("No")
else:
    for i in S:
        if s[i]==2:
            pass
        else:
            print("No")
            break
    else:
        print("Yes")