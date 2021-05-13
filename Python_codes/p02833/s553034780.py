N = int(input())
if N % 2:
    print(0)
    exit()
N = N//2
ans = 0
while N:
    ans += N // 5
    N //= 5
print(ans)