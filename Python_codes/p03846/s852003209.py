n = int(input())
a = list(map(int, input().split()))
mod = (10**9)+7
w = [0]*n
for i in a:
    w[i] += 1
if (n%2==1):
    if (w[0]!=1):
        print(0)
        exit()
    for i in range(1,n):
        if (i%2==1):
            if (w[i]>0):
                print(0)
                exit()
        else:
            if (w[i]!=2):
                print(0)
                exit()
    print(pow(2,n//2,mod))
else:
    if (w[0]!=0):
        print(0)
        exit()
    for i in range(1,n):
        if (i%2==0):
            if (w[i]>0):
                print(0)
                exit()
        else:
            if (w[i]!=2):
                print(0)
                exit()
    print(pow(2,n//2,mod))