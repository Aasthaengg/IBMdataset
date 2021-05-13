N, M = map(int, input().split())

ans, pre = 0, 0
i = 1
while True:
    pre = ans
    ans += i*(1900*M+100*(N-M))*(((2**M-1)/2**M)**(i-1))/(2**M)
    i += 1
    if ans - pre < 10**(-2):
        break
print(int(round(ans, 0)))
