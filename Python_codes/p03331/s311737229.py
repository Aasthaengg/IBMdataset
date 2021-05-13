N = int(input())
ans  = 10**5+1
for i in range(1,N//2 + 1):
    A = i
    B = N - i
    tmp = 0
    while(A > 0):
        tmp += A % 10
        A //= 10
    while(B > 0):
        tmp += B % 10
        B //= 10
    ans = min(ans,tmp)
print(str(ans))