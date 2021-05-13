n=input()
num=map(int,raw_input().split())
max=-1000000
min=1000000
sum=0
for i in range(n):
    if max<num[i]:
        max=num[i]
    if min>num[i]:
        min=num[i]
    sum+=num[i]
print str(min)+" "+str(max)+" "+str(sum)