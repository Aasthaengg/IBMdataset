S = list(input())
T = list(input())
NS,NT = len(S),len(T)
outs = []
if NS>=NT:
    for i in range(NS-NT+1):
        flag = 0
        for j in range(NT):
            if S[i+j]==T[j] or S[i+j]=="?":
                continue
            else:
                flag = 1
                break
        if flag==0:
            out = ["a"]*NS
            for j in range(NT):
                out[i+j]=T[j]
            for j in range(NS):
                if S[j]!="?":
                    out[j]=S[j]
            outs.append("".join(out))

if len(outs) == 0:
    print("UNRESTORABLE")
else:
    print(outs[-1])