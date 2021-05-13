m,k=map(int,input().split())

if m == 1 and k == 0:
    print("0 0 1 1")
    quit()
k += (2**(m) == 2 and k == 1)
if k< 2**(m):
    l = list(range(2**(m)))
    r = l[::-1]
    tep = [k]
    res=l[:k] + l[k+1:] +tep + r[:2**m-k-1] + r[2**m-k:] + tep
    s = ""
    for j in res:
        s+=str(j)+" "
    print(s[:-1])
else:
    print(-1)