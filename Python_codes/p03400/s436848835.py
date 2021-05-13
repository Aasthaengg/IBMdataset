n = int(input())
d, x = [int(i) for i in input().split()]
a = [int(input()) for i in range(n)]

ans = x + n + sum([ d // i if d % i != 0 else d // i -1 for i in a])
print(ans)
