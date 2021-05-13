N = int(input())

def d_sum(n):
    ret = 0
    while(n>0):
        ret += n%10
        n //= 10
    return ret

ans = N
for i in range(1, N//2+2):
    ans = min(ans, d_sum(i)+d_sum(N-i))

print(ans)
