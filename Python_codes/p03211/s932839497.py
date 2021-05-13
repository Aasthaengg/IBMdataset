S = input()
MIN = 1000
for T in range(0,len(S)-2):
    X = int(S[T:T+3])
    Num = abs(X-753)
    if Num<MIN:
        MIN = Num
print(MIN)