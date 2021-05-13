a,b=(int(x) for x in input().split())
sum=0
while a>0:
    a-=b
    sum+=1
print(sum)