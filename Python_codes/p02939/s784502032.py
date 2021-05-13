S=input()
tmp = S[0]
n = ""
ans = 1
for i in S[1:]:
    n += i
    if tmp != n:
        ans += 1
        tmp = n
        n = ""
print(ans)