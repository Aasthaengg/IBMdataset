n,k=map(int,input().split())
h=[]
for i in range(n):
    h.append(int(input()))
h.sort()
m=float('inf')
for i in range(len(h)-k+1):
    m=min(m,h[i+k-1]-h[i])
print(m)