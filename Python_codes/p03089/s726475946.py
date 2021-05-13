n = int(input())
b = list(map(int, input().split()))

c = sorted(b)

for i in range(n):
    if b[i] > i + 1:
        print(-1)
        exit()

ans = []

for i in range(n):
    s = b[i]
    ans.insert(s-1, s)

print(*ans) 