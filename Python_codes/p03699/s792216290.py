n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
ans = sum(s)
s.sort()
if ans%10 == 0:
    mi = ans
    for i in range(n):
        if s[i]%10 != 0:
            mi = s[i]
            break
    ans -= mi
print(ans)