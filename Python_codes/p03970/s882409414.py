S = input()
target = "CODEFESTIVAL2016"

ans = 0
for s, t in zip(S, target):
    if s != t:
        ans += 1
print(ans)
