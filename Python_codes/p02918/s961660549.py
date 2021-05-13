n, k = map(int, input().split())
s = list(input())
cnt = 0
tmp = s[0]
t = 0
for i in range(1, n):
    if tmp == s[i]:
        continue
    else:
        cnt += 1
        tmp = s[i]
c = 0
for i in range(1, n):
    if s[i] == s[i-1]:
        c += 1
if cnt <= 2*k:
    print(n-1)
else:
    print(c + 2*k)