N, M = map(int, input().split())

real = M - 2*N

if real < 0:
    ans = M // 2
elif real == 0:
    ans = real
else:
    a = real // 4
    ans = a + N

print(ans)