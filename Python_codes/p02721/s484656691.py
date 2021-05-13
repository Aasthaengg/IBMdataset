N, K, C = map(int, input().split())
S = input()
L = [-1] * K
R = [-1] * K
L_index = 0
L_count = 0
R_index = N - 1
R_count = K - 1

while L_index < N and L_count < K:
    if S[L_index] == "o":
        L[L_count] = L_index
        L_index += (C + 1)
        L_count += 1
    else:
        L_index += 1
while R_index >= 0 and R_count >= 0:
    if S[R_index] == "o":
        R[R_count] = R_index
        R_index -= (C + 1)
        R_count -= 1
    else:
        R_index -= 1

for i in range(K):
    if L[i] == R[i]:
        print(L[i] + 1)
