S = input()
#Aの探索
for i in range(len(S)):
    if S[i] == "A":
        S = S[i:]
        break

#Zの探索
if S[-1] == "Z":
    print(len(S))
    exit()
for i in range(1, len(S)+1):
    if S[-i] == "Z":
        S = S[:-i+1]
        break
print(len(S))