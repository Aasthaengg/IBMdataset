n = int(input())
ans = 0
flag = True if n == 1 else False

tmp = 0
while n % 2 == 0:
    n //= 2
    tmp += 1
i = 0
while tmp >= (i+1)*(i+2)//2:
    i += 1
ans += i

idx = 3
while n > idx**2:
    tmp = 0
    if n % idx == 0:
        while n % idx == 0:
            n //= idx
            tmp += 1
        i = 1
        while tmp >= (i+1)*(i+2)//2:
            i += 1
        ans += i
    idx += 2

print(0 if flag else (ans+1 if n > 1 else ans))