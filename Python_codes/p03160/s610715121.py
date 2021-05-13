n=int(input())
a=list(map(int,input().split()))

dp_table=[]
for i in range(n):
    if i==0:dp_table.append(0)
    elif i==1:dp_table.append(abs(a[i]-a[i-1]))
    else:dp_table.append(min(abs(a[i]-a[i-2])+dp_table[-2],abs(a[i]-a[i-1])+dp_table[-1]))
print(dp_table[-1])