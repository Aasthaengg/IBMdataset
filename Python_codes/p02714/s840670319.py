N = int(input())
S = input()

num_R = S.count('R')
num_G = S.count('G')
num_B = S.count('B')
S = '_' + S

count = 0
for i in range(1, N+1):
    for j in range(i, N+1):
        k = 2*j - i
        if j <= k and k <= N:
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                count += 1
#                 print(i, j, k)
print(num_R*num_G*num_B - count)