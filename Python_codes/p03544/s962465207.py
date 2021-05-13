n = int(input())
l0 = 2
l1 = 1
if n == 0:
    print(l0)
elif n == 1:
    print(l1)
elif n>= 2:
    ll = [l0, l1] + [0 for _ in range(n-1)]
    for i in range(2,n+1):
        ll[i] = ll[i-1] + ll[i-2]
    print(ll[n])
