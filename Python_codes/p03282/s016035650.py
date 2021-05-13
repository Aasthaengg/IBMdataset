import sys

S=input()
K=int(input())

for s in S[:min(len(S),K)]:
    if s=="1":
        pass
    else:
        print(s)
        sys.exit()
print(1)
        
