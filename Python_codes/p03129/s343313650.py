N, K = map(int, input().split())
if N % 2 == 0:
    ans = int(N / 2)
else:
    ans = int(N / 2) + 1
if K <= ans:
    print("YES")
else:
    print("NO")
