n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = []
for i in range(n-k):
    if (a[i] < a[i+k]):
        ans.append("Yes")
    else:
        ans.append("No")

for i in range(len(ans)):
    print(ans[i])
