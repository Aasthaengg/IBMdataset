# coding: utf-8

N = int(input())
S = input()

# ruisekiwa ba-jon

ruiseki_w = [0] * (N + 1)
ruiseki_e = [0] * (N + 1)

for i in range(0, len(S)):
    ruiseki_w[i+1] = ruiseki_w[i] + S[i].count("W")
    ruiseki_e[i+1] = ruiseki_e[i] + S[i].count("E")

res = 10**10
for i in range(0, len(S)):
    hidari_no_w_no_kazu = ruiseki_w[i]
    migi_no_e_no_kazu = ruiseki_e[-1] - ruiseki_e[i+1]
    res = min(hidari_no_w_no_kazu + migi_no_e_no_kazu, res)

print(res)
