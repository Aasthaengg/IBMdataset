def turn_check(inlist,p,q,x):
    s = q*x
    t = p-q
    return sum([ (max(i-s,0)+t-1)//t for i in inlist ]) <= x

n, a, b = [ int(v) for v in input().split() ]
h_list = [ int(input()) for i in range(n) ]
ok, ng = 10**9, 0
while ok-ng > 1:
    mid = (ok+ng)//2
    if turn_check(h_list,a,b,mid):
        ok = mid
    else:
        ng = mid
print(ok)
