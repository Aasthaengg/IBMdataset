S = input()
A = "CODEFESTIVAL2016"
ans = 0
for s, a in zip(S, A):
    ans += (s != a)

print(ans)
