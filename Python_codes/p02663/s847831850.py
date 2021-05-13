import math
h_one,m_one,h_two,m_two,k = map(int,input().split())

hour = h_two - (h_one + 1)
minute = (60 - m_one) + m_two

print(60*hour + minute - k)