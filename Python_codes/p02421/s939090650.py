# coding: utf-8
n = int(input())
t_p = 0
h_p = 0

for _ in range(n):
    t_w, h_w = input().split()
    if t_w > h_w:
        t_p += 3
    elif h_w > t_w:
        h_p += 3
    else:
        t_p += 1
        h_p += 1
        
print(t_p, h_p)