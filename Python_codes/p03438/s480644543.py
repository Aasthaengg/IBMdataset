n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ope = 0
for i in range(n):
    if b[i] > a[i]:
        ope+=(b[i]-a[i]+1)//2

if sum(b) - sum(a) < 0:
    print('No')        
elif ope <= sum(b) - sum(a):
    print('Yes')
else:
    print('No')