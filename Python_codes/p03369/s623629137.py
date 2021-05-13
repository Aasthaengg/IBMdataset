S = input()

val = 700

for i in range(len(S)):
    if S[i] == 'o':
        val += 100

print(val)
