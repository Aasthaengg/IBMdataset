n = int(input())
s = str(input())
ans = 0
for i in range(n-3+1):
    if s[i:i+3] == 'ABC': ans += 1
print(ans)