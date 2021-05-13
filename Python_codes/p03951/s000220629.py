n = int(input())
s = input()
t = input()
ans = s+t
for i in range(n):
    if s[i] == t[0]:
        if s[i:] == t[:n-i]:
            ans = s[:i]+t
            break
print(len(ans))