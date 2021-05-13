def l_in(type_): return list(map(type_, input().split()))
def i_in(): return int(input())
def m_in(type_): return map(type_, input().split())
def r_in(n, type_): return [type_(input()) for _ in range(n)]
ans = False
a, b, c = m_in(int)
k = i_in()
for _ in range(k):
    if c <= b or c <= a: c *= 2
    elif b <= a: b *= 2
    if c > b > a:
        ans = True
        break
print('Yes' if ans else 'No')