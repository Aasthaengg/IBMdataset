l, d, r = map(int, input().split())
ans = []
for i in range(l, d+1):
    if i % r == 0:
        ans.append(i)

print(len(ans))
