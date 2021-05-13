n,K=(int(i) for i in input().strip().split(" "))
x=[int(i) for i in input().strip().split(" ")]
m=1000000000000000000000
for i in range(n-K+1):
    k=-x[i]+x[i+K-1]+min(abs(x[i]),abs(x[i+K-1]))
    if k<m:
        m=k
print(m)