import bisect

n = int(input())
d = list(map(int,input().split()))
m = int(input())
t = list(map(int,input().split()))

d.sort()
t.sort()

set_t = list(set(t))


for i in range(len(set_t)):
    n_d = bisect.bisect_right(d,set_t[i]) - bisect.bisect_left(d,set_t[i])
    n_t = bisect.bisect_right(t,set_t[i]) - bisect.bisect_left(t,set_t[i])
    
    if n_t > n_d:
        print('NO')
        exit()

print('YES')