n = int(input())
s = input().split(" ")
S = list(map(int,s))
q = int(input())
t = input().split(" ")
T = list(map(int,t))
C = []
for i in range(n):
    flag = 0
    for k in range(len(C)):
        if S[i] == C[k]:
            flag = 1
            break
    if flag == 1:
        continue
    for j in range(q):
        if S[i] == T[j]:
            C.append(S[i])
            break
print(len(C))