import sys
n,k = map(int,input().split())
ls = list(map(int,input().split()))
p = len(list(set(ls)))
if p <= k:
    print(0)
    sys.exit()
di=[float("inf")]*n
for i in range(n):
    if di[ls[i]-1] == float("inf"):
        di[ls[i]-1] = 1
    else:
        di[ls[i]-1] += 1
di.sort(reverse=True)
q = 0 
while True:
    s = di.pop()
    p -= 1
    q += s
    if p <= k:
        print(q)
        sys.exit()