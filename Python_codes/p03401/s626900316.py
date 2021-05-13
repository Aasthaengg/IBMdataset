n=int(input())
a=[0]+list(map(int,input().split()))+[0]

sumD=0
for i in range(1,len(a)):
    sumD+=abs(a[i]-a[i-1])

for g in range(n):
    print(sumD-abs(a[g+2]-a[g+1])-abs(a[g+1]-a[g])+abs(a[g+2]-a[g]))