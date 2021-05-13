n, k = map(int, input().split())
r,s,p = map(int, input().split())
t = input()
point = {"s":r, "p":s, "r":p}
x = {"s":"r", "p":"s", "r":"p"}
ans = []
P = 0
for i in t:
    if len(ans) < k or ans[-k] != x[i]:
        ans.append(x[i])
        P += point[i]
    else: ans.append("")
print(P)  