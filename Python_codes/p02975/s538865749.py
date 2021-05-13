n=int(input())
a=list(map(int,input().split()))
num=a[0]
for i in range(1,n):
    num=num^a[i]
if max(a)==(2**(n-3))+(2**(n-4)):
    print("No")
elif max(a)==min(a) and a[0]!=0:
    print("No")
elif num<=1:
    print("Yes")
else:
    print("No")
