from copy import deepcopy
n = int(input())
S = input()

accum = [[0,0,0]]
dic = {"R": 0, "G": 1, "B": 2}
accum[0][dic[S[0]]] += 1
for i in range(1, n):
    new_e = deepcopy(accum[i-1])
    new_e[dic[S[i]]] += 1
    accum.append(new_e)
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if S[i] != S[j]:
            if (S[i] == "R" and S[j] == "G") or (S[i] == "G" and S[j] == "R"): 
                ans += accum[n-1][dic["B"]] - accum[j][dic["B"]]
                a = dic["B"]
            elif (S[i] == "R" and S[j] == "B") or (S[i] == "B" and S[j] == "R"):
                ans += accum[n-1][dic["G"]] - accum[j][dic["G"]]
                a = dic["G"]
            else:
                ans += accum[n-1][dic["R"]] - accum[j][dic["R"]]
                a = dic["R"]
            if j + j - i < n and j + j - i > j:
                ans -= accum[j+j-i][a] - accum[j+j-i-1][a]
print(ans)