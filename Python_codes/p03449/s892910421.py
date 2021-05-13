NN = int(input())
AA1 = list(map(int,input().split()))
AA2 = list(map(int,input().split()))

SS = [0]*NN

SS[0] = AA1[0] + sum(AA2)
for ii in range(1, NN-1):
    SS[ii] = SS[ii-1] - AA2[ii-1] + AA1[ii]
SS[NN-1] = sum(AA1) + AA2[NN-1]

print(max(SS))
