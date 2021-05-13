n=int(input())
a=list(map(int,input().split()))
p=0
for _ in range(n):
    p+=(1/a[_])
print("{:.6f}".format(1/p));