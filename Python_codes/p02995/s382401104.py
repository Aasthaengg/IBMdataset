from math import floor, ceil, gcd

a,b,c,d = map(int, input().split())

if a%c == 0: c_m_min = a
else: c_m_min = a + c - a%c
c_m_max = b - b%c
c_cnt = (c_m_max - c_m_min)//c + 1
if c_m_min > b or c_m_max < a : c_cnt = 0

if a%d == 0: d_m_min = a
else: d_m_min = a + d - a%d
d_m_max = b - b%d
d_cnt = (d_m_max - d_m_min)//d + 1
if d_m_min > b or d_m_max < a : d_cnt = 0

cd = c*d//gcd(c,d)
if a%cd == 0: cd_m_min = a
else: cd_m_min = a + cd - a%cd
cd_m_max = b - b%cd
cd_cnt = (cd_m_max - cd_m_min)//cd + 1
if cd_m_min > b or cd_m_max < a : cd_cnt = 0


ans = b - a + 1 - c_cnt - d_cnt + cd_cnt
print(ans)