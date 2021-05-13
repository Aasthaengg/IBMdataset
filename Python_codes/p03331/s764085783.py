n = int(input())

ans = 10**10
for i in range(1,n):
    a = i
    b = n-i
    s = sum([int(i) for i in str(a)]) + sum([int(i) for i in str(b)])
    ans = min(ans,s)
print(ans)