n=int(input())
h=list(map(int, input().split()))
out=0
m=0
for i in range(1,n):
    if h[i-1]>=h[i]:
        m+=1
    else:
        m=0
    if m>out:
        out=m
print(out)