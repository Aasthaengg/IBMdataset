N = int(input())
S = input()
max = 0

for i in range(1,N):
    dicl = {}
    dicr = {}
    for j in range(i):
        dicl[S[j]] = j
    for j in range(i,N):
        if(S[j] in dicl.keys()):
            dicr[S[j]] = j
    if len(dicr.keys()) > max:
        max = len(dicr.keys())
print(max)