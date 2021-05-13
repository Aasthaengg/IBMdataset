S = input()
l = len(S)
mozi = []
for i in range(l):
    mozi.append(S[i])
mozi = list(set(mozi))
C = [chr(i) for i in range(ord("a"),ord("z")+1)]

for i in mozi:
    for j in C:
        if i == j:
            C.remove(j)
if len(C) == 0:
    print("None")
else:
    print(C[0])