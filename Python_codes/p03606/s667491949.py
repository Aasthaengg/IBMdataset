n=int(input())
min=[]
max=[]
mem=0
for i in range(n):
    min1,max1=[int(i) for i in input().split()]
    min.append(min1)
    max.append(max1)
    mem+=max[i]-min[i]+1
print(mem)