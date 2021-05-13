p,q,r = map(int,input().split())
pq = p+q
qr = q+r
rp = r+p
print(min(pq,qr,rp))