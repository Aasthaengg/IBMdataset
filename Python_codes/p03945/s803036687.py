S = input()
c = 0
if set(S) == 0:
    print(0)
else:
    for i in range(len(S) - 1):
        if S[i] != S[i + 1]:
            c += 1
print(c)
