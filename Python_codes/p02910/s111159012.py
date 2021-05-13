import sys
S = input()
for i in range(0, len(S), +2):
    if S[i] == "L":
        print("No")
        sys.exit()    
if len(S) == 1:
    print("Yes")
    sys.exit()
for i in range(1, len(S), +2):
    if S[i] == "R":
        print("No")
        sys.exit()
print("Yes")
