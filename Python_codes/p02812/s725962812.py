N = input()
S = input()
T = "ABC"

res=0
for i in range(0, len(S)):
    if S[i:i+len(T)]==T:
        res+=1

print(res)