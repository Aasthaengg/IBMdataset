S = input()

old = 1<<60
for i in range(len(S)-2):
    T = int(S[i:i+3])
    
    if old > abs(T-753):
        old = abs(T-753)


print(old)