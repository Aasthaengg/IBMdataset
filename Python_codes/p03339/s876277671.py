n = int(input())
s = input()
left = 0
right = s[1:].count('E')
cnt = [left + right]

for i in range(1, n):
    if s[i-1] == 'W':
        left += 1
    if s[i] == 'E':
        right -= 1
    cnt.append(left + right)

print(min(cnt))