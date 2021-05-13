n=int(input())
h=list(map(int,input().split()))
c=[0]
for i in range(n-1):
    x=abs(h[i]-h[i+1])+c[i]
    y=x+1
    if i>0:
        y=abs(h[i-1]-h[i+1])+c[i-1]
    c.append(x if x<y else y)
print(c[n-1])