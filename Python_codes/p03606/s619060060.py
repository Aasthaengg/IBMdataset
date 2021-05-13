n=int(input())
list=[]
for i in range(n):
    l,r=map(int,input().split())
    list.append(l)
    list.append(r)
#print(list)
sum=0
for i in range(int(len(list)/2)):
    sum+=list[2*i+1]-list[2*i]+1
print(sum)