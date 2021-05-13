S = input()
K = int(input())

l = 0
for i in range(len(S)):
    if S[i] == '1':
        l += 1
    if l >= K:
        print(S[i])
        exit()
    if S[i] != '1':
        print(S[i])
        exit()
