n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
cnt1=[0]*n
cnt2=[0]*n
for i in range(n):
    if a[i]>b[i]:
        cnt2[i]=a[i]-b[i]
    else:
        num4=b[i]-a[i]
        cnt1[i]=-(num4//-2)
        cnt2[i]=num4%2
num5=abs(sum(a)-sum(b))
if max(sum(cnt1),sum(cnt2))+abs(sum(cnt1)-sum(cnt2))<=num5:
    print("Yes")
else:
    print("No")
