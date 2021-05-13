S = input()
for T in range(len(S)-2,0,-2):
    if S[:T//2]==S[T//2:T]:
        print(T)
        break