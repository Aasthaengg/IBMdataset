import math
import sys
S=input()
count=0
for i in range(len(S)):
    if S[i]=="o":
        count+=1
    if count>=8:
        print("YES")
        sys.exit()
if len(S)<15:
    count+=15-len(S)
    if count>=8:
        print("YES")
        sys.exit()
print("NO")