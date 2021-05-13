import sys

S = input()

da = ""

for i in range(len(S)):

    if S[i] != "A":
        da += S[i]

if da != "KIHBR":
    print ("NO")
    sys.exit()

last = ""
na = 0
for i in range(len(S)):

    if S[i] == "A":
        na += 1

    else:
        last = S[i]
        na = 0

    if (last in ["","H","B","R"] and na > 1 ) or (last in ["K","I"] and na > 0):
        print ("NO")
        sys.exit()

print ("YES")
