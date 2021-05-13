N = int(input())
if N % 2 == 1:
    print(0)
    exit()
tmp = 2
ans = 0
while tmp < N:
    tmp *= 5
    ans += N // tmp
print(ans)