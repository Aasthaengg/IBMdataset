k, x = map(int, input().split())
ans = [x]
for sign in [-1, 1]:
    for i in range(1, k):
        ans.append(x + sign*i)

ans.sort()
for i in range(len(ans)):
    print(ans[i], end=" ")