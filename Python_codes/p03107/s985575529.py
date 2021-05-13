
S = input()
N = len(S)
cnt0 = S.count("0")
cnt1 = S.count("1")
ans = 2*min(cnt0, cnt1)
print(ans)

