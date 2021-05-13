N,T = map(int,input().split())
t = list(map(int,input().split()))
tdiff = [t[i+1]-t[i] for i in range(N-1)]
tsum = T
for i in tdiff:
    if T > i:
        tsum += i
    else:
        tsum += T
print(tsum)