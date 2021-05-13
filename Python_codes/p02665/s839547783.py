n = int(input())
a = list(map(int,input().split()))
b = [0]*(n+1)
if n == 0:  
    x = a[0]
    if x == 1:
        print(1)
    else:
        print(-1)
    exit()
nows = sum(a)
s = nows
for i in range(n+1):
    if i == 0:
        b[i] = 1 - a[i]
    else:
        nows -= a[i]
        b[i] = min(nows, 2*b[i-1]-a[i])
        if b[i] < 0:  
            print(-1)
            exit()

print(sum(b)+s)  
