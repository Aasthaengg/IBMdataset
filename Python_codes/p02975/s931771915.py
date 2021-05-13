n=int(input())
a=sorted(list(map(int,input().split())))

if n%3==0:
    for j in range(3):
        for i in range(j*(n//3),(j+1)*(n//3)-1):
            if a[i]!=a[i+1]:
                print("No")
                exit()
    if a[0]^a[n//3]==a[2*n//3]:
        print("Yes")
    else:
        print("No")
    exit()
for i in range(0,n-1):
    if a[i]!=a[i+1]:
        print("No")
        exit()
print("Yes")