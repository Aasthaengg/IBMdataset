import sys

S = list(input())
K = int(input())

for i in range(len(S)):
    if i+1 <= K and S[i] != '1':
        print(S[i])
        sys.exit()

print(1)