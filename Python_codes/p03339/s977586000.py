n = int(input())
S = input()
W = [0] * (n+1)
w = 0
ans = float("inf")

for i in range(n):
    if S[i] == "W":
        w += 1
    
    W[i+1] = w
    
for i in range(n):
    res = W[i] + ((n-W[n]) - (i+1-W[i+1]))
    ans = min(ans,res)
    
print(ans)