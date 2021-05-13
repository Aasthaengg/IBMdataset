s = list(input())
M = []

for i in range(len(s)):
    if i % 2 == 0:
        M.append(s[i])
        
ANS = ''.join(M)
print(ANS)