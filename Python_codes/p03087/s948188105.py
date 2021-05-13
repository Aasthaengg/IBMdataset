n, q = map(int,input().split())
s = list(input())
lr = [list(map(int,input().split())) for i in range(q)]
ans = [0]
x = 0

for i in range(n-1):
    if s[i] == "A" and s[i+1] == "C":
        x += 1
    ans.append(x)

for i in lr:
    l = i[0]
    r = i[1]
    print(ans[r-1] - ans[l-1])
