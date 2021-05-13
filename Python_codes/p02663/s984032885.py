h1, m1, h2, m2, k = map(int, input().split())
t1, t2 = h1*60+m1, h2*60+m2
if t1 > t2:
    t2 += 60*24
ans = t2-t1-k
print(ans)