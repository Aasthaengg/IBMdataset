H1, M1, H2, M2, K = map(int, input().split())
if H1 == H2:
    ans = M2 - M1
else:
    ans = (H2 - H1) * 60
    ans += M2 - M1
ans -= K
print(ans)
