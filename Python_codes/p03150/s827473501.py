S=input()
N=len(S)
if S=="keyence":
    print("YES")
    exit()
for i in range(N):
    for j in range(i,N):
        tmp=""
        for k in range(N):
            if i<=k and k<=j:
                continue
            tmp=tmp+S[k]
        if tmp=="keyence":
            print("YES")
            exit()

print("NO")