
si = lambda: input().strip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
lmsi = lambda: list(map(str, input().split()))
smii = lambda: sorted(map(int, input().split()))

# ----------

S = si()

ans = 0
ans += S.count('+')
ans -= S.count('-')

print(ans)