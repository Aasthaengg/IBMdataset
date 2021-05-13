n = int(input())
l = list(map(int,input().split()))
l.sort()
mod = 10**9+7
if n % 2 == 1:
    if l[0] != 0:
        print(0)
        exit()
    count = 2
    for i in range(1,n-1,2):
        
        if l[i] != count or l[i] != l[i+1]:
            print(0)
            exit()
        count += 2
    print(pow(2,n//2,mod))
else:
    count = 1
    for i in range(0,n-1,2):
        if l[i] != count or l[i] != l[i+1]:
            print(0)
            exit()
        count += 2
    print(pow(2,n//2,mod))
