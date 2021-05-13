N = int(input())
S = list(input())
ans = ''
for i in S:
    ans = ans + chr(65 + (ord(i) + N - 65)%26)

print(ans)