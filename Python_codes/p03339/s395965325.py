NN = int(input())
SS = str(input())

score = [0]*NN
for i in range(1,NN):
    if SS[i] == "E":
        score[0] += 1

for pos in range(1,NN-1):
    score[pos] = score[pos-1]
    if SS[pos-1] == "W":
        score[pos] += 1
    if SS[pos] == "E":
        score[pos] -= 1

score[NN-1] = score[NN-2]
if SS[NN-2] == "W":
    score[NN-1] += 1
if SS[NN-1] == "E":
    score[NN-1] -= 1

print(min(score))