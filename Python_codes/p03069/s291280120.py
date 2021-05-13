n = int(input())
s = input()

b = [0 for k in range(n+1)]
c = 0
for k in range(n):
    if s[k] == "#":
        c += 1
    b[k+1] = c

w = [0 for k in range(n+1)]
c = 0
for k in range(n):
    if s[-k-1] == ".":
        c += 1
    w[-k-2] = c

ans = 10**9
for k in range(n+1):
    ans = min(ans,b[k]+w[k])

print(ans)
