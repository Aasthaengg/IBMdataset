n = int(input())
a = list(map(int, input().split()))

k = len(set(a))
if k % 2:
    ans = k
else:
    ans = k - 1

print(ans)
