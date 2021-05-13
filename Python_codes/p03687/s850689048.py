from collections import Counter

A = list(input())
S = A
MIN = 2000
for t in set(A):
    count = 0
    S = A
    while count <= MIN:
        if len(set(S)) == 1:
            MIN = min(count,MIN)
            break
        T = [None] * (len(S)-1)
        for i in range(len(T)):
            if S[i] == t or S[i+1] == t:
                T[i] = t
            else:
                T[i] = S[i]

        S = T
        count += 1


print(MIN)
