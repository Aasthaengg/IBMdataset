n,k = (int(a) for a in input().split())
h = sorted(list(map(int, input().split())))
if n <= k :
    print(0)
else :
    print(sum(h[:(n-k)]))
