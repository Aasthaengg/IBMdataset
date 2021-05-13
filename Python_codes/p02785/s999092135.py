n,k = map(int,input().split())

h = list(map(int,input().split()))

h.sort(reverse=True)

if k == 0 :
    print(sum(h))
elif k <= n :
    for i in range(k):
        h[i] = 0
    print(sum(h))
else :
    print(0)
