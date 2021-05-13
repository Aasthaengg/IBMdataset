N = int(input())
S = input()
 
r = S.count('R')
g = S.count('G')
b = S.count('B')
 
c = 0
for i in range(N):
    for j in range(i+1, N):
        h = 2*j-i
        if h >= N:
            break
        if S[i]!=S[h] and S[i]!=S[j] and S[j]!=S[h]:
            c += 1
 
print(r*g*b-c)