n = int(input())
S = input()
ans = ''
for s in S:
    if ord(s) + n <= 90:
        ans += chr(ord(s) + n)
    else:
        ans += chr(65 + ord(s) + n - 90 - 1)
print(ans)
