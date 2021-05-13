s = input()
ans = 1000000

for i in range(len(s)-2):
    S = s[i]+s[i+1]+s[i+2]
    S = int(S)
    q = abs(753-S)
    ans = min(ans, q)

print(ans)