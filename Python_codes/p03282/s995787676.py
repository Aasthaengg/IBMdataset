S = input()
K = int(input())

i = 0
while i < K - 1 and S[i] == '1':
    i += 1
print(S[i])