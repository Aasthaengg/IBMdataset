N = int(input())

if N % 2 != 0:
    print(0)
    exit(0)

ans = 0
a = 10
while True:
    if N < a:
        break

    ans += N//a
    a *= 5
print(ans)
