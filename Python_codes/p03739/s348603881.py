n = int(input())
a = list(map(int,input().split()))

s = [0,0]
ans = [0,0]
# [0]:+ - + - ... [1]:- + - + - ...

for i in range(n):
    s[0] += a[i]
    s[1] += a[i]
    if s[0]*pow(-1,i) <= 0:
        ans[0] += 1 - s[0]*pow(-1,i)
        s[0] = pow(-1,i)
    if s[1]*pow(-1,i) >= 0:
        ans[1] += s[1]*pow(-1,i) + 1
        s[1] = -pow(-1,i)
print(min(ans))
