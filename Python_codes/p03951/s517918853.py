n = int(input())
s = input()
t = input()
ans = ""
for i in range(n):
    if s[i] == t[0]:
        if s[i:] == t[:n-i]:
            ans = s[:i]+t
            break
if ans == "": ans = s+t
print(len(ans))