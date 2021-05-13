s = input()
n = len(s)
ans = 1000
for i in range(n-2):
    a = '' + s[i] + s[i+1] + s[i+2]
    a = int(a)
    ans = min(ans, abs(a - 753))
print(ans)