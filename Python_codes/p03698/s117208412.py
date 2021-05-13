S = input().strip()
C = {}
for i in range(len(S)):
    a = S[i]
    if a not in C:
        C[a] = 0
    C[a] += 1
if len(S)==len(C):
    print("yes")
else:
    print("no")