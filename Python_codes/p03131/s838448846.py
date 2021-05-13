K, A, B = map(int, input().split())

bisc = 1
yen = 0

ans = K + 1

if A >= B:
    print(ans)
    exit()

now = A
K -= (A - 1)
now += (K // 2) * (B - A)
K = K % 2
now += K
print(max(now, ans))