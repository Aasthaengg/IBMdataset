n,a,b=map(int,input().split())
h=[]
for i in range(n):
    q=int(input())
    h.append(q)
left=0
right=max(h)+1
def en(t):
    cnt=0
    for i in range(n):
        if h[i]-b*t>0 and (h[i]-b*t)%(a-b)!=0:
            cnt+=((h[i]-b*t)//((a-b))+1)
        if h[i]-b*t>0 and (h[i]-b*t)%(a-b)==0:
            cnt+=((h[i]-b*t)//(a-b))
    if cnt<=t:
        return  True
    return  False
while left+1<right:
    tmp=(left+right)//2
    if en(tmp):
        right=tmp
    else:
        left=tmp
print(right)
