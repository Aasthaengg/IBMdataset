n, m = map(int, input().split())

ans_time = (n-m) * 100
ans = (2**m) * (1900*m + ans_time)
print(ans)