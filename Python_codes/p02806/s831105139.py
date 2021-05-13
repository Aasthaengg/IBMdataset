N = int(input())
A = [list(input().split()) for i in range(N)]
X = input()
b = 0
ans = 0
for a in A:
    if b == 0:
        if a[0] == X:
            b = 1
    else:
        ans += int(a[1])
print(ans)