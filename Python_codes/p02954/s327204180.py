s = input()

ans = [0] * len(s)

cnt = 0
for i in range(len(s)):
    if s[i] == 'R':
        cnt += 1
        continue
    even = cnt // 2
    odd = cnt - even
    ans[i-1] += odd
    ans[i] += even
    cnt = 0

cnt = 0
for i in range(len(s)-1, -1, -1):
    if s[i] == 'L':
        cnt += 1
        continue
    even = cnt // 2
    odd= cnt - even
    ans[i] += even
    ans[i+1] += odd
    cnt = 0

print(*ans, sep=' ')