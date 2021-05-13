N = int(input())
X = list(map(int,input().split()))
ans = 10**36
S = 0

for p in range(100):
    S =0
    for x in X:
        S += (x-p)**2
    ans = min(ans,S)

print(ans)