a=map(int,raw_input().split())
if min(a[2],a[3])>=a[4] and a[2]+a[4]<=a[0] and a[3]+a[4]<=a[1]: print("Yes")
else:print("No")