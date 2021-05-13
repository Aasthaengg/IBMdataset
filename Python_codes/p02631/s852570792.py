n = int(input())
a = list(map(int, input().split()))

tmp = 0
for aa in a:
    tmp ^= aa
ans = [tmp ^ aa for aa in a]
print(*ans)