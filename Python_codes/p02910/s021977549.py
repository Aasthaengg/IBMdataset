import sys
S = input()

for i in range(len(S)):
    if (i%2==0 and S[i] in ["R", "U", "D"]) or (i%2!=0 and S[i] in ["L", "U", "D"]):
        continue
    else:
        print("No")
        sys.exit()
print("Yes")