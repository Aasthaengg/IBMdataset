s = input()
ans = 'NO'
pattern = 'keyence'

for i in range(len(pattern) + 1):
    x = s[:i]
    y = s[::-1][:len(pattern) - i][::-1]
    if x + y == pattern:
        ans = 'YES'
        break

print(ans)
