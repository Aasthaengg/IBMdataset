n, k = map(int, input().split())
s = input()

cnt = 0
prev = ''

for i in range(len(s)):
    if s[i] == prev:
        cnt += 1
    else:
        prev = s[i]

print(min(cnt + 2 * k, n - 1))
