n = int(input())
a = list(map(int, input().split()))
arr = [False] * n

for i in range(n, 0, -1):
    if sum(arr[i - 1::i]) % 2 != a[i - 1]:
        arr[i - 1] = True

if not any(arr):
    print(0)
else:
    print(sum(arr))
    ans = []
    for i, x in enumerate(arr):
        if x:
            ans.append(i + 1)
    print(*ans)