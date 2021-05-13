S = list(input())
T = list(input())
N = len(S)
dicS={}
dicT={}
for i in range(97,123,1):
    dicS[chr(i)] = []
    dicT[chr(i)] = []

for i in range(0,N,1):
    dicS[S[i]].append(i)
    dicT[T[i]].append(i)

for a2z in dicS:
    if len(dicS[a2z])>0:
        tmp = T[dicS[a2z][0]]
        for i in range(0,len(dicS[a2z]),1):
            if T[dicS[a2z][i]]!=tmp:
                print("No")
                exit()
    if len(dicT[a2z])>0:
        tmp = S[dicT[a2z][0]]
        for i in range(0,len(dicT[a2z]),1):
            if tmp != S[dicT[a2z][i]]:
                print("No")
                exit()

print("Yes")
