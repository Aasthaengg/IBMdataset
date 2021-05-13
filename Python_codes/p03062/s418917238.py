n = int(input())
a = list(map(int, input().split()))
p = sum(ai < 0 for ai in a)
ans = sum(map(abs, a))
if p & 1:
    ans -= 2 * min(abs(ai) for ai in a)
print(ans)
