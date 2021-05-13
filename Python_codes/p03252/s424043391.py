S=input()
T=input()

Rs = {}
Rt = {}

for s,t in zip(S,T):
    
    if s in Rs.keys() and Rs[s] != t:
        print("No")
        exit()
    if t in Rt.keys() and Rt[t] != s:
        print("No")
        exit()

    if not s in Rs.keys():
        Rs[s] = t
    if not t in Rt.keys():
        Rt[t] = s

ress = [""] * len(S)
rest = [""] * len(S)
for i,s in enumerate(S):
    ress[i] = Rs[s]

for i,t in enumerate(T):
    rest[i] = Rt[t]
print("Yes" if "".join(ress)==T and "".join(rest)==S else "No")