n = int(input())
a = list(map(int, input().split()))

ans = [0 for _ in range(n)]

for i in range(n):
    p = False
    for j in range(len(a)-1, -1, -1):
        if a[j] == j+1:
            ans[n-1-i] = a.pop(j)
            p = True
            break

    if not p:
        print(-1)
        exit()

for ai in ans:
    print(ai)