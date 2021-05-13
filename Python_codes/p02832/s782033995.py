n = int(input())
A = list(map(int, input().split()))

i = 1
ans = 0
red = []
for a in A:
    if a == i:
        red += [i]
        i += 1
    else:
        ans += 1
if not ans == len(A):
    print(ans)
else:
    print(-1)