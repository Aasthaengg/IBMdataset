S = input()
N = len(S)//2
for l in range(N-1, 0, -1):
    if S[:l] == S[l:l*2]:
        print(l*2)
        break