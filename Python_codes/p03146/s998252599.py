def judge(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1

s = int(input())
ans = 1

while s != 4 and s != 2 and s != 1:
    s = judge(s)
    ans += 1

print(ans+3)