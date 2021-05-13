n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = list(input())

for i in range(k,n):
    if t[i] == t[i-k]:
        t[i] = "0"

ans = [0] * n

for i in range(n):
    if t[i] == "r":
        ans[i] = p
    elif t[i] == "s":
        ans[i] = r
    elif t[i] == "p":
        ans[i] = s

print(sum(ans))
