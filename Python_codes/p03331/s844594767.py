n = int(input())
ans = 2*10**5
for i in range(1,n):
    a = i
    b = n - i
    ans = min(ans, sum([int(c) for c in str(a)+str(b)]))
print(ans)