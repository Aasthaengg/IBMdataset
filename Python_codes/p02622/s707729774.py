# B Minor Change
S = list(input())
T = list(input())
l =len(S)
ct = 0
for i in range(l):
    if S[i] != T[i]:
        ct += 1
print(ct)