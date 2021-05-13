n=int(input())
h=list(map(int,input().split()))
s=0
t=0
for i in range(n-1):
    if h[i]>=h[i+1]:
        s+=1
    else:
        if s>=t:
            t=s
        s=0
if s>=t:
    t=s
print(t)