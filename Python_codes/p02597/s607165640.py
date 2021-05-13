n = int(input())
c = input()
r = 0
left, right = 0, n-1
while left < right:
    if c[left] == 'W' and c[right] == 'R':
        r += 1
        left += 1
        right -= 1
    if c[left]=='R':
        left += 1
    if c[right]=='W':
        right -= 1
print(r)