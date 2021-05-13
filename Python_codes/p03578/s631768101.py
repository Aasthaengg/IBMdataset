n=int(input())
d=list(map(int, input().split()))
m=int(input())
t=list(map(int, input().split()))

from collections import Counter
d_c=Counter(d)
t_c=Counter(t)

flag=True
for key in t_c:
    if d_c[key]<t_c[key]:
        flag=False
print('YES' if flag else 'NO')
