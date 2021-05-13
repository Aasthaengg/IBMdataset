n = int(input())
s = input()
t = input()

ans = ""
for i in range(n):
    if s[i] == t[0] and s[i:] == t[:n-i]:
        ans = s[:i]+t
        break
print(n*2 if ans=="" else len(ans))