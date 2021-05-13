S = input()
T = input()

min_length = 10000
len_def = len(S) - len(T)
for i in range(len_def + 1):
    counter = 0
    for j in range(len(T)):
        if S[j + i] != T[j]:
            counter += 1

    if counter < min_length:
        min_length = counter
print(min_length)
