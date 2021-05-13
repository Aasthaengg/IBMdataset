n,k = map(int,input().split())
h = sorted([int(input()) for _ in range(n)])
salist = []
for i in range(n-k+1):
    salist += [h[k-1+i]-h[i]]

print(min(salist))