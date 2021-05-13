n,k=map(int,input().split())
h=[]
for i in range(n):
    h1=int(input())
    h.append(h1)
h.sort()
s=10000000000
for i in range(n-k+1):
    if s>h[i+k-1]-h[i]:
        s=h[i+k-1]-h[i]
print(s)