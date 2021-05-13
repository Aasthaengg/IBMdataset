N = int(input())
M=0
ans = 1
for i in range(1,N+1):
    num = i
    tmp = 0
    while(num % 2 == 0):
        tmp += 1
        num /= 2
    if M < tmp:
        M = tmp
        ans = i
print(ans)

