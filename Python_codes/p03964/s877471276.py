n = int(input())
nt  =0
na = 0
for _ in range(n):
    t,a = map(int,input().split())
    if nt==0 and na==0:
        nt =t
        na =a
        continue
    if na <= nt*(a/t):
        mod = nt%t
        if not mod==0:
            mod = t - mod
            nt = nt + mod
            na = a*nt//t
        else:
           nt = nt
           na = a*nt//t
    else:
        mod = na%a
        if not mod==0:
            mod = a - mod
            na = na + mod
            nt = t*na//a
        else:
           na = na
           nt = na*t//a 
        

print(na+nt)