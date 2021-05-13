a, b, k = map(int, input().split())
ans = []
for i in range(k):
    if a + i <= b:
        ans.append(a + i)
for j in range(b - k + 1, b + 1):
    if j not in ans and a <= b - k + 1:
        ans.append(j)
for k in range(len(ans)):
    print(ans[k])
