def l_in(type_): return list(map(type_, input().split()))
def i_in(): return int(input())
def m_in(type_): return map(type_, input().split())
def r_in(n, type_): return [type_(input()) for _ in range(n)]
ans = None

a, b, c, d = m_in(int)
ans = max(a*c, a*d, b*c, b*d)

print(ans)
