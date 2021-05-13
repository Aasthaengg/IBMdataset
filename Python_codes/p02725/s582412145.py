k,n = map(int,input().split())
a = list(map(int,input().split()))
aa = a + a

for j in range(n,2*n):
    aa[j] = aa[j] + k

dis = k

for i in range((2*n)-1):
    tonari = aa[i+1]-aa[i]
    dis = min(dis,k-tonari)

print(dis)