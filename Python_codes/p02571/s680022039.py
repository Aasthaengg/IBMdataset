#-*- Coding: utf-8 -*-

S = input()
T = input()

X = []
for i in range(len(S)-len(T)+1):
    c = 0
    for j in range(len(T)):
        if S[i+j] == T[j]:
            c += 1
    X.append(c)
print(len(T) - max(X))
