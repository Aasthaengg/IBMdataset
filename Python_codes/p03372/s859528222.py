n,C=map(int,input().split())
que=[]
for _ in range(n):
    x,v=map(int,input().split())
    que.append((x,v))

dpl=[0 for i in range(n+1)] #dpl[i]=左からi番目に行くまでのお腹の値のプラス
dpr=[0 for i in range(n+1)] #dpr[j]＝右からj番目に行くまでのお腹の値のプラス

c=0
for i in  range(n):
    c+=que[i][1]
    dpl[i+1]=c-que[i][0]

d=0
for i in range(1,n+1):
    d+=que[-i][1]
    dpr[i]=d-(C-que[-i][0])

max1=max(dpl)
max2=max(dpr)

dpb_l=[0 for i in range(n+1)]#dpb_l[i]=左からi番目に行って戻るときに達成できるお腹の値のプラス
dpb_r=[0 for i in range(n+1)]#dpb_r[i]=右からi番目に行って戻るときに達成できるお腹の値のプラス

c=0

for i in  range(n):
    c+=que[i][1]
    dpb_l[i+1]=c-2*que[i][0]

d=0
for i in range(1,n+1):
    d+=que[-i][1]

    dpb_r[i]=d-2*(C-que[-i][0])

#dpl[i]=左からi番目のところに行くまでに達成できるお腹の値のプラスの最大値
#dpr[i]=右からi番目のところに行くまでに達成できるお腹のあたいのプラスの最大値

for i in range(1,n+1):
    dpl[i]=max(dpl[i-1],dpl[i])
for i in range(1,n+1):
    dpr[i]=max(dpr[i],dpr[i-1])

max3=0

for i in range(1,n):
    max3=max(max3,dpb_l[i]+dpr[n-i],dpb_r[i]+dpl[n-i])

print(max(max1,max2,max3))


