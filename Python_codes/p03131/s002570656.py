K, A, B = map(int, input().split())

if B - A <= 2 or A + 1 > K:
    print(K + 1)
    exit()

K -= A - 1
res = A

res += (B - A) * (K // 2)

if K % 2 == 1:
    res += 1

print(res)
