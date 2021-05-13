a,b=list(map(int,input().split()))
d=b-a
sum=0
l=[]
for i in range(1,d):
    sum+=i
    l.append(sum)
print(sum-a)
