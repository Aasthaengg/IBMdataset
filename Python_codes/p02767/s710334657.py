N = int(input())
X = list(map(int,input().split()))
ans = 10**9
for k in range(min(X),max(X)+1):
    temp = 0
    for e in X:
        temp += (k-e)**2
    ans = min(temp,ans)
print(ans)
