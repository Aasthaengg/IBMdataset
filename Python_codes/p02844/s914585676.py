n = int(input())
#a, b, c, x, y = map(int, input().split())
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]
s = list(input())
ans = 0


for i in range(1000):
    t = ''
    t += str(i % 10)
    t += str((i//10) % 10)
    t += str(i//100)
    t = t[::-1]
    i = 0
    j = 0
    while i < n and j < 3:
        if s[i] == t[j]:
            j += 1
        i += 1
    if j == 3:
        ans += 1
print(ans)
