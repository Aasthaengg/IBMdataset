# ABC048 B Between a and b...

a, b, x = map(int,input().split())

_a = a//x
m_a = a%x
_b = b//x

if m_a == 0:
    print(_b - _a + 1)
else:
    print(_b - _a)