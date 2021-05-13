N = int(input())

ans = 0
if N > 3:
    ans += N-1

for i in range(2, int(N**0.5)+1):
    if N%i == 0:
        a = i-1
        if N//a == N%a:
            ans += a
        a = N//i-1
        if N//a == N%a:
            ans += a

print(ans)