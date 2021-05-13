S = input()
S_num = [0]*len(S)

for i in range(len(S)):
    if S[i] in ["A", "T", "G", "C"] :
        if i == 0:
            S_num[i] = 1
        else:
            S_num[i] = S_num[i-1]+1

print(max(S_num))