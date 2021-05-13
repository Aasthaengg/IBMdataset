n = int(input())
s = input()

ans = 0
# when 0-th person is the leader
for i in range(1, n):
    if s[i] == 'E':
        ans += 1

tmp = ans
# when i-th person is the leader
for i in range(1, n):
    if s[i-1] == 'W':
        tmp += 1
    if s[i] == 'E':
        tmp -= 1
    ans = min(ans, tmp)


print(ans)