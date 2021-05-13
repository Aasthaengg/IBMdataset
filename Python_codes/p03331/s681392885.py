n = int(input())
ans = 10**5
for i in range(n//2):
    a = i+1
    b = n-a
    tmp = 0
    for i in str(a):
        tmp += int(i)
    for i in str(b):
        tmp += int(i)
    ans = min(ans, tmp)
print(ans)