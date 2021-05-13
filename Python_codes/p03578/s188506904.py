import collections

n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

d_c = collections.Counter(d)
t_c = collections.Counter(t)

ans = 'YES'
for e in t_c.items():
    if d_c[e[0]]:
        if d_c[e[0]] < e[1]:
            ans = 'NO'
            break
    else:
        ans = 'NO'
        break
    
print(ans)