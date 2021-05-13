n = int(input())
l = list(map(int,input().split()))
l.sort()
a=l[0]
count=0
for i in range(1,n):
    count=(a+l[i])/2
    a=(a+l[i])/2
print(count)