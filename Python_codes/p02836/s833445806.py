S = input()
S_r = S[::-1]
print(sum(S[i]!=S_r[i] for i in range(len(S)))//2)