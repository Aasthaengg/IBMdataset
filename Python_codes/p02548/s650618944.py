n = int(input())

ans = 0

for a in range(1, n):
    t = (n-1) // a
    ans += t

print(int(ans))
