S = input().strip()
C = {}
for i in range(len(S)):
    if S[i] not in C:
        C[S[i]] = 0
    C[S[i]] += 1
if len(C)==2:
    flag = 0
    for a in C:
        if C[a]!=2:
            flag = 1
            break
    if flag==0:
        print("Yes")
    else:
        print("No")
else:
    print("No")