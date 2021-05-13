n=int(input())
a=[int(x) for x in map(int,input().split()[:n])]
ret=a[0]
for x in range(1,n):
    ret= a[x] ^ ret
if ret==0:
    print("Yes")
else:
    print("No")