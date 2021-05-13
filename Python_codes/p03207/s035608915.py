n = int(input())

mxvalue = 0
ans = 0
for i in range(n):
    p = int(input())
    ans += p
    mxvalue = max(mxvalue, p)
print(ans - (mxvalue // 2))