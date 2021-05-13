n = int(input())
s = input()
t = input()

for i in range(n):
    if t.startswith(s[i:]):
        ans = s[:i]+t
        break
    else:
        ans = s+t

print(len(ans))