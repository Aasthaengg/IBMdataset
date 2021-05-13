S = []
H = []
C = []
D = []
for i in range(14):
    S.append(False)
    H.append(False)
    C.append(False)
    D.append(False)
n = input()
for i in range(n):
    c, a = raw_input().split()
    if(c == "S"):
        S[int(a)] = True
    elif(c == "H"):
        H[int(a)] = True
    elif(c == "C"):
        C[int(a)] = True
    elif(c == "D"):
        D[int(a)] = True
for i in range(1, 14):
    if(S[i] == False):
        print("S %d" %(i))
for i in range(1, 14):
    if(H[i] == False):
        print("H %d" %(i))
for i in range(1, 14):
    if(C[i] == False):
        print("C %d" %(i))
for i in range(1, 14):
    if(D[i] == False):
        print("D %d" %(i))