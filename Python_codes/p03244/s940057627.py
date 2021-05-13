import collections
N =int(input())
V =list(map(int,input().split()))
ev_col = collections.Counter(V[::2]).most_common()
od_col = collections.Counter(V[1::2]).most_common()
 
if ev_col[0][0] != od_col[0][0]:
    ans = N - od_col[0][1] - ev_col[0][1]
else:
    if len(ev_col) >= 2 and len(od_col)  >= 2:
        if ev_col[1][1] >= od_col[1][1]:
            ans = N - ev_col[1][1] - od_col[0][1]
        else:
            ans = N - od_col[1][1] - ev_col[0][1]
    else:
        ans = N - ev_col[0][1]
print(ans)