N_1 = int(input())
A = [str(input()) for i in range(N_1)]
N_2 = int(input())
B = [str(input()) for i in range(N_2)]

C = A+B
D = list(set(C))
E=[]
for i in range(len(D)):
    NN = A.count(D[i]) - B.count(D[i])
    E.append(NN)
if max(E)>=0:
    print(max(E))
else:
    print(0)