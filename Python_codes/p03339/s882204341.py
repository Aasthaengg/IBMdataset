import sys
input = sys.stdin.readline

N = int(input())
S = input()

W_num = [0] * N
E_num = [0] * N

for i in range(1, N):
    k = N - (i - 1) - 2
    W_num[i] = W_num[i-1] + 1 if S[i-1] == 'W' else W_num[i-1]
    E_num[k] = E_num[k+1] + 1 if S[k+1] == 'E' else E_num[k+1]

print(min([W_num[i] + E_num[i] for i in range(N)]))
