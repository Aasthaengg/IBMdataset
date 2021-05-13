N = int(input())
ans = 0

if N % 2 == 1:
    print(0)
    exit()

tmp = 2 * 5
while N >= tmp:
    ans += N // tmp
    tmp *= 5
print(ans)