h,w = map(int,input().split())
a = [input() for _ in range(h)]

a_set = set()
for i in range(h):
    for j in range(w):
        a_set.add(a[i][j])

odd = 0
mul_2 = 0
for s in a_set:
    tmp = 0
    for i in range(h):
        tmp += a[i].count(s)
    odd += (tmp%2 == 1) * 1
    mul_2 += ((tmp%2 == 0) & (tmp%4 == 2)) * 1


limit_odd = ( h*w % 2 == 1) * 1
limit_mul_2 = (h%2 == 1) * (w//2) + (w%2 == 1) * (h//2)
if((odd <= limit_odd) & (mul_2 <= limit_mul_2)):
    print('Yes')
else:
    print('No')