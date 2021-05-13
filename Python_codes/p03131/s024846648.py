K, A, B = map(int, input().split())
if B - A <= 2:
    print(K + 1)
    exit()
count = K - A + 1
ans = A + (count // 2) * (B - A) + count % 2
print(ans)
