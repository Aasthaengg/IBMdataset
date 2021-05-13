N = int(input())
N_List = []
for i in range(N):
    N_List.append(int(input()))
NMax = max(N_List)
if N_List.count(NMax) == 1:
    NMax2 = sorted(N_List)[-2]
    for i in N_List:
        print((NMax,NMax2)[i==NMax])
else:
    for i in N_List:
        print(NMax)