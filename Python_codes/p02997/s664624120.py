import sys
n,k = map(int,input().split())


if k > (n-1)*(n-2)/2:
    print(-1)
    sys.exit()

num = (n-1)*(n-2)/2 - k
print(int(n-1+num))
ansl = []
for i in range(1,n):
    print(str(1)+" "+str(i+1))

for i in range(1,n):
    for j in range(i+1, n):
        if num > 0:
            print(str(i+1)+" "+str(j+1))
            num -= 1

