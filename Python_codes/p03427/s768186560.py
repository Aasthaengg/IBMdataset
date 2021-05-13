N = int(input())
a = 0
b = 0
while N > 0:
    if N < 10:
        c = N
        break
    if N % 10 != 9:
        b = 1
    N //= 10
    a += 1
if b == 1:
    c -= 1
ans = c + a * 9
print(ans)
