S = input()

N = len(S)

for i in range(N-2, 0, -2):
    h = i // 2
    if S[:h] == S[h:i]:
        
        print(i)
        break