n = int(input())
ab = []
for i in range(n):
    ab.append(tuple(map(int,input().split())))
ab.sort(key=lambda x: x[1])
m = 0
ans = "Yes"
for ai,bi in ab:
    m += ai
    if m > bi:
        ans = "No"
print(ans)
