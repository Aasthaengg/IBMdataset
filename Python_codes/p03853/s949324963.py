h, w = map(int, input().split())
ans = list()
for a in range(h):
    c = input()
    ans.append(c)
    ans.append(c)

for a in range(h*2):
    print(ans[a])
