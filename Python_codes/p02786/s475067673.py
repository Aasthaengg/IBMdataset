N = int(input())

if N == 1:
    print(1)
else:
    ans = 1
    i = 1
    while N >= 2 ** i:
        ans += 2 ** i
        i += 1
    print(ans)