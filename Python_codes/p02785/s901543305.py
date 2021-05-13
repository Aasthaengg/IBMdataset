n,k=list(map(int, input().split()))
h = list(map(int, input().split()))
h.sort()
keep = n-k
if keep < 0:
    print(0)
else:
    print(sum(h[:keep]))
