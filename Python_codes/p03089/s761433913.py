n = int(input())
a = list(map(int, input().split()))
ans = []

for i in range(n):
    delete = max([a[j] if (j == a[j] - 1) else 0 for j in range(len(a))])
    if (delete == 0):
        print(-1)
        exit()
    else:
        ans.append(delete)
        a.pop(delete-1)

for i in reversed(ans):
    print(i)