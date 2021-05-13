n=int(input())
a=list(map(int,input().split()))
l=[sum(a)-sum(a[1::2])*2]
for i in range(1,n):
 l.append(a[i-1]*2-l[i-1])
print(*l)