n,k = map(int,input().split())
ls = list(map(int,input().split()))
fi = [-1]*(n+1)
fi[1] = 0
a = 0
aa = 0
for i in range(k):
    if fi[ls[a]] == -1:
        fi[ls[a]] = i + 1
        aa = a
        a = ls[a] - 1
    else:
        ind = fi[ls[a]]
        t = (k - ind) % (max(fi) + 1 - ind)
        t += ind
        print(fi.index(t))
        break
else:
    print(ls[aa])