N = int(input())
a = 0
b = 0
ans = 0
s = 10000
for i in range(1,int(N/2) + 1):
    a = i
    b = N - i
    ans = 0
    while 1:
        ans += a % 10 + b % 10
        a = a // 10
        b = b // 10
        if a == 0 and b == 0:
            if ans < s:
                s = ans
            break
print(s)
