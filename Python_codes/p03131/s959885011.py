K, A, B = map(int, input().split())
ans = 1
ans += min(K, A-1)
K -= min(K, A-1)
if K == 0:
    print(ans)
elif B-A > 2:
    if K % 2 == 0:
        print(ans + (B-A) * K // 2)
    else:
        print(ans + (B-A) * (K-1) // 2 + 1)
else:
    print(ans+K)
