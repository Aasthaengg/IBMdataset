n,m = map(int,input().split())

# n + x : m - 2 * x = 1 : 2
# 2n+2x = m - 2x
# 4x = m-2n

if n * 2 <= m:
    l = (m - 2 * n) // 4
    ans1 = min(n+l, (m-l*2)//2)
    ans2 = min(n+l+1, (m - (l+1)*2)//2)
    print(max(ans1, ans2))

else:
    print(m//2)
