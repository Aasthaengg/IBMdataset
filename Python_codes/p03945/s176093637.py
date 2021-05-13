S = input()

s = S[0]
for i in range(1, len(S)):
    if s[-1] != S[i]:
        s += S[i]

if len(S) == 1:
    print(0)
    exit(0)
elif len(S) == 2:
    print(1)
    exit(0)

print(len(s)-1)
