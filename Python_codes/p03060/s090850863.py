n = int(input())
xlist = list(map(int,input().split()))
ylist = list(map(int,input().split()))

sum = 0
for i in range(n):
  if xlist[i]-ylist[i]>=0:
    sum += xlist[i]-ylist[i]
    
print(sum)