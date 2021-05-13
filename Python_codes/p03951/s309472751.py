n = int(input())
s = str(input())
t = str(input())

temp = 0
for i in range(n+1):
    if t[0:i] == s[n-i:n]:
        temp = i

ans = 2*n-temp
print(ans)
