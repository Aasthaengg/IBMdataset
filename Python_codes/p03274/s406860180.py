n,k = map(int,input().split())
x = list(map(int,input().split()))
times = []
for i in range(n-k+1):
    tl =abs(x[i])
    tr = abs(x[i+k-1])
    tw = abs(x[i]-x[i+k-1])
    times.append(min(tl,tr)+tw)
print(min(times)) 