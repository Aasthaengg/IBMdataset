n=int(input())

h=list(map(int,input().split()))

c=[0]*n 
for i in range(1,n):
    if h[i]<= h[i-1]:
        c[i]=c[i-1]+1

v=c[0]
for i in range(n):
    if c[i]>v:
        v=c[i]
print(v)    