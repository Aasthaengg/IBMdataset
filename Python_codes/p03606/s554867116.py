n = int(input())
ans = sum([r - l + 1 for l, r in [[int(x) for x in input().split()] for _ in range(n)]])
print(ans)