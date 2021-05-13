def solve(bi, ei, bs):
    mid = (bi+ei)//2
    print(mid, flush=True)
    s = input()
    if s=='Vacant':
        exit(0)
    elif (s==bs)^((mid-bi)%2):
        solve(mid, ei, s)
    else:
        solve(bi, mid, bs)

n = int(input())
print(0, flush=True)
s = input()
if s=='Vacant':
    exit(0)
solve(0, n, s)