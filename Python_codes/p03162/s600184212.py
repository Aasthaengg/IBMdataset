from sys import stdin
n = int(stdin.readline())
a,b,c = [],[],[]
for _ in range(n):
    A,B,C = map(int,stdin.readline().split())
    a.append(A)
    b.append(B)
    c.append(C)
dpa,dpb,dpc = [a[0]],[b[0]],[c[0]]
for i in range(1,n):
    dpa.append(a[i]+max(dpb[i-1],dpc[i-1]))
    dpb.append(b[i]+max(dpa[i-1],dpc[i-1]))
    dpc.append(c[i]+max(dpb[i-1],dpa[i-1]))
print(max(dpa[-1],dpb[-1],dpc[-1]))
