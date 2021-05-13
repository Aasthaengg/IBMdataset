n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    if a[i] > i + 1:
        print(-1)
        exit()
for i in range(n):
    for i in range(n - i)[-1::-1]:
        if a[i] == i + 1:
            ans.append(a[i])
            del a[i]
            break
for i in ans[-1::-1]:
    print(i)