n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]
arr = list(range(1, d + 1))
ans = 0

for i in a:
    emp = arr[::i]
    ans += len(emp)

print(ans + x)
