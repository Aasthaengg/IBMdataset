xs = [int(i) for i in input().split()]
k = int(input())

x = max(xs)
ans = x * (2**k) + sum(xs) - x

print(ans)
