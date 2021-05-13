S = list(input())
for i in range(len(S)//2):
    S.pop()
    S.pop()
    if S[:len(S)//2] == S[len(S)//2:]:
        print(len(S))
        exit()