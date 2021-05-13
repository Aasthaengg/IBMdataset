n = int(input())
*a, = map(int, input().split())

ave = sum(a)/n

ans = []
for i, _a in enumerate(a):
    ans.append([abs(ave-_a), i])

ans.sort()
print(ans[0][1])
