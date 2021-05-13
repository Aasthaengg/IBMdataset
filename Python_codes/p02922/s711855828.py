A,B=map(int,input().split())
n=1
count=0
while n<B:
    n+=(A-1)
    count+=1
print(count)