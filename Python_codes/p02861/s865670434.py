def dist(a,b):
    return ((b[0]-a[0])**2+(b[1]-a[1])**2)**(1/2)
n=int(input())
loca=[list(map(int, input().split())) for _ in range(n)]
import itertools
a=[i for i in range(n)]
sum=0
cnt=0
for i in itertools.permutations(a):
    li=list(i)
    cnt += 1
    for i in range(1,n):
        a=loca[li[i-1]]
        b=loca[li[i]]
        sum+=dist(a,b)
print(sum/cnt)