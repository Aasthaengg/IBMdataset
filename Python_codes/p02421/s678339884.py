n = int(input())
p_t = 0
p_h = 0
for i in range(n):
    c_t,c_h = map(str,input().split())
    if c_t > c_h:
        p_t += 3
    elif c_t < c_h:
        p_h += 3
    else:
        p_t += 1
        p_h += 1
print(p_t,p_h)