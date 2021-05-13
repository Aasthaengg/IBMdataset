n = int(input())
An = list(map(int, input().split()))
An.sort()
ans = 1
for i in range(0,n):
    ans = ans * An[i]
    if ans > 10**18:
        ans = -1
        break

    if An[i] == 0:
        break

print(ans)
