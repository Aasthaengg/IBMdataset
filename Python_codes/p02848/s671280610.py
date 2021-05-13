N = int(input())
S = input()
ans = ''
for s in list(S):
    ans += chr((ord(s) + N) % 91 + (65 if (ord(s) + N) % 91 < 65 else 0))
print(ans)
