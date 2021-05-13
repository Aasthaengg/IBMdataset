n = int(input())
a = list(input().split())
num = list(range(n-1,-(n-1)-2,-2) )
for i in range(len(num)):
    if num[i]<0:
        num[i] = abs(num[i]+1)
    print(a[num[i]], end = ' ')