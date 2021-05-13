n = int(input())
s = input()
right, left = 0, s.count('.')
r = [left]
for i in range(n):
    if s[i]=='#':
        right += 1
    else:
        left -= 1
    r.append(right+left)
print(min(r))