#31
import sys
S = input()
l = len(S)

for i in range(l):
    cou = 0
    for j in range(l):
        if S[i] == S[j]:
            cou +=1
    if cou == 2:
        print("no")
        sys.exit()
print("yes")