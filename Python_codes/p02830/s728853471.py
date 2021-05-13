N = int(input())
S, T = input().split()
char = ''

for i in range(N):
    char = S[i] + char
    char = T[i] + char

print(char[::-1])
