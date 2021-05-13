n = int(input())
h = list(map(int, input().split()))
l = [0] + h + [0]
n += 2
ans = 0
while sum(l) != 0:
    for i in range(1, n):
        if (l[i] == 0) and (l[i-1] != 0):
            ans += 1
    for i in range(1, n):
        if l[i] != 0:
            l[i] -= 1
print(ans)