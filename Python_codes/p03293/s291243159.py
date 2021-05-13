import sys
S = str(input())
T = str(input())


for i in range(len(S)):
    S = S[-1]+S[:-1]
    if S == T:    
        print("Yes")
        sys.exit()
print("No")