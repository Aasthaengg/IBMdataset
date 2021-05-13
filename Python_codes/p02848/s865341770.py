N = int(input())
S = input()

ans = ''
for i in S:
    n = ord(i) + N
    if n > 90:
        n -= 26
    ans += chr(n)
print(ans)