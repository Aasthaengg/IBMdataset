n = int(input())
la = [int(w) for w in input().split()]

ans = 0
i = 1
for a in la:
    if a != i:
        ans += 1
    else:
        i += 1
if ans == n and i == 1:
    ans = -1

print(ans)
