N, K = map(int, input().split())
if N % 2 == 0 and K <= (N // 2):
    print("YES")
elif N % 2 == 1 and K <= ((N // 2) + 1):
    print("YES")
else:
    print("NO")