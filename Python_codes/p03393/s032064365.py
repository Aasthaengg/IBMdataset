from string import ascii_lowercase
S = input()
N = len(S)
if N < 26:
    for char in ascii_lowercase:
        if char in S: continue
        print(S + char)
        exit()
if S == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit()
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if S[i] < S[j]:
            print(S[:i] + S[j])
            exit()
