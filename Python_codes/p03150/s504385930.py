import sys
S = input()


for i in range(len(S)):
    for j in range(i,len(S)):
        
        if "keyence" == (S[:i]) + (S[j:]):
            print("YES")
            sys.exit()

print("NO")