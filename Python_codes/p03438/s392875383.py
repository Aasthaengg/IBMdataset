n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

max_cnt=sum(b)-sum(a)
if max_cnt<0:
    print("No")
    exit()
b_cnt=0
a_cnt=0
for i in range(n):
    if a[i]>b[i]:
        b_cnt+=a[i]-b[i]
    elif a[i]<b[i]:
        a_cnt+=(b[i]-a[i])//2
print("Yes" if b_cnt<=a_cnt else "No")

