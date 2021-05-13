X = int(input())
a = X // 100
r = X % 100
ans = '1' if r <= 5*a else '0'
print(ans)