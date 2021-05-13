# -*- coding: utf-8 -*-
num,h_target,m_target = map(int,input().split())
#cnt_2_in_str = lambda x: 1 if x == '2' else 0

h_list,m_list = [],[]
for i in range(0,num):
    h,m = map(int,input().split())
    h_list.append(h)
    m_list.append(m)

cnt = 0
for i in range(0,num):
    if h_list[i] >= h_target and m_list[i] >= m_target:
        cnt += 1

print(cnt)