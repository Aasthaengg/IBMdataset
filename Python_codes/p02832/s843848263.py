n = int(input())
A = list(map(int, input().split()))
i = 1
ans = n
for a in A:
    if a == i:
        i += 1
        ans -= 1
print(ans if ans != n else -1)