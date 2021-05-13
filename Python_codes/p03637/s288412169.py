n = int(input())
a = list(map(int,input().split()))
n4 = 0
n2 = 0
for i in range(n):
    if a[i]%4==0:
        n4+=1
    elif a[i]%2==0:
        n2+=1
if n2 ==1:
    n2 = 0
l = n4*2 + n2
if l>=n or n4*2+1 == n:
    print('Yes')
else:
    print('No')
