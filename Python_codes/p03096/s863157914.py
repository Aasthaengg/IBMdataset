n = int(input(""))
mod = 1e9+7
maxn = 200000
x = []
f = []
sum = [0 for j in range(0,maxn+1)]
def add(a,b):
    s = (a+b)%mod
    return s
f.append(1)
x.append(-1)
for i in range(1,n+1):
    x.append(int(input()))
    if(x[i]==x[i-1]):
        f.append(f[i-1])
    else :
        f.append(add(f[i-1],sum[x[i]]))
        sum[x[i]]=f[i]
print(int(f[n]))