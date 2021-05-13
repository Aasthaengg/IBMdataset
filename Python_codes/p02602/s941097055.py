
n, k = (int(x) for x in input().split())
a = input().split()

for i in range(1,n-k+1):
    if(int(a[i-1]) >= int(a[k+i-1])):
        print("No")
    else:
        print("Yes")