#! python3
#  solve_122B.py

S = input()

t = [0]*len(S)

if S[0] in ["A","C","G","T"]:
    t[0] = 1

for i in range(1,len(S)):
    if S[i] in ["A","C","T","G"]:
        t[i] = t[i-1] + 1
    else:
        t[i] = 0

print(max(t))