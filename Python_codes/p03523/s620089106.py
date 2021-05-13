import sys
S = list(input())

L = list("KIHBR")
for l in L:
    if not l in "".join(S):
        print("NO")
        sys.exit(0)

N = []
for i in range(len(S)-1):
    if S[i] == "H" or S[i] == "B" or S[i] == "R":
        if S[i+1] != "A":
            N.append(i+1)

i = 0
for n in N:
    S.insert(n+i, "A")
    i += 1
    
if "".join(S) in "AKIHABARA":
    print("YES")
else:
    print("NO")