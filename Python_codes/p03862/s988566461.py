n,x=map(int,input().split())
a = list(map(int,input().split()))

nec = [0 for i in range(n)]
fi = max(-x+(a[0]+a[1]),0)
nec[1] = max(0,a[1]-fi)
for i in range(2,n):
    sec = max(-x+(a[i]+nec[i-1]),0)
    nec[i]=a[i]-sec
    fi += sec

print(fi)
