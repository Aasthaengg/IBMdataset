N = int(input())
a = list(map(int, input().split()))
frag = 0
ans = 0
while True:
    for i in range(N):
        if a[i] % 2 == 1:
            frag = 1
            break
    if frag == 0:
        for i in range(N):
            a[i] /= 2
        ans += 1
    else:
        break
print(ans)
