A, B, C, K = map(int, input().split())

ans = A-B if K % 2 == 0 else B-A

print(ans)