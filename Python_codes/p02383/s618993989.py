ls = list(map(int,input().split()))
S = input()
for i in range(len(S)):
    if S[i] == "N":
        ls[0],ls[1],ls[5],ls[4] = ls[1],ls[5],ls[4],ls[0]
    if S[i] == "E":
        ls[0],ls[3],ls[5],ls[2] = ls[3],ls[5],ls[2],ls[0]
    if S[i] == "W":
        ls[0],ls[3],ls[5],ls[2] = ls[2],ls[0],ls[3],ls[5]
    if S[i] == "S":
        ls[0],ls[1],ls[5],ls[4] = ls[4],ls[0],ls[1],ls[5]
print(ls[0])
