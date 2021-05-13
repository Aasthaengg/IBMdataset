N=int(input())
XL=sorted([list(map(int,input().split())) for i in range(N)],key=lambda x: x[0]+x[1])
r,a=-10**9,0
for x,l in XL:
    if r<=x-l:
        a+=1
        r=x+l
print(a)