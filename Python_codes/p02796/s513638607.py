N=int(input())
XL=sorted([list(map(int,input().split())) for i in range(N)],key=sum)
count=0
left=-10**9
for x,l in XL:
    if left<=x-l:
        count+=1
        left=x+l
print(count)