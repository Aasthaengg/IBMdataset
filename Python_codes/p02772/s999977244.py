n = int(input())
a = list(map(int,input().strip().split()))[:n]
flag = True
for i in range(0,n):
    if a[i]% 2 == 0:
        if a[i]% 3 != 0 and a[i]% 5 != 0:
            flag = False
if  flag==True:
    print("APPROVED")
else :
    print("DENIED")