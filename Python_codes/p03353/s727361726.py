s = input()
k = int(input())
n = len(list(s))
kouho = set()
for i in range(n):
    for d in range(1, k + 1):
        if i + d <= n:
            kouho.add(s[i : i + d])
ans = list(kouho)
ans.sort()
# print(ans)
print(ans[k - 1])
