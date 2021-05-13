n = int(input())
a = list(map(int,input().split()))
a1=0
m = [0]*n
for i in range(n):
    a1+=(-1)**i*a[i]
m[0]=str(a1)
for i in range(1,n):
    m[i]=str((a[i-1]-int(m[i-1])//2)*2)
print(' '.join(m))
