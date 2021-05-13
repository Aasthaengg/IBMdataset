H1, M1, H2, M2, K = map(int, input().split())

hk = K//60
mk = K%60

ans = (H2 - hk)*60 + (M2 - mk) - (H1*60 + M1)
print(max(ans, 0))