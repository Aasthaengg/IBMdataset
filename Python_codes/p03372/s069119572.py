n,c=map(int, input().split())
a = [[0,0]]+[list(map(int, input().split())) for i in range(n)]
l=[[0,0] for i in range(n+1)]
r=[[0,0] for i in range(n+1)]
b = 0
b1 = 0
# 最大値を格納
x=[0]*(n+1)
y=[0]*(n+1)
ans=0
ansl=0
ansr=0

#  時計周りで累積和を取る。折り返しがない時の最大値を探す。
ans1=-10**20
ans2=-10**20
for i in range(n+1):
    b+=a[i][1]
    l[i][0]=a[i][0]
    l[i][1]=b
    if b-l[i][0]>ans1:
        ans1=b-a[i][0]
        x[i]=ans1
    else:
        x[i]=x[i-1]

for i in range(n+1):
    b1+=a[-i][1]
    r[i][0]=c-a[-i][0]
    r[i][1]=b1
    if b1-r[i][0]>ans2:
        ans2=b1-r[i][0]
        y[i]=ans2
    else:
        y[i]=y[i-1]
r[0][0]=0
y[0]=0


# 反時計周りで折り返して時計周りへ進む
for i in range(n):
    cnt=x[n-i]+r[i][1]-2*r[i][0]
    ansr=max(cnt,ansr)

# 時計周りで折り返して反時計周りへ進む
for i in range(n):
    cnt=y[n-i]+l[i][1]-2*l[i][0]
    ansl=max(cnt,ansl)
print(max(ansr,ansl))