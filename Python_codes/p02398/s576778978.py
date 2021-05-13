count=0
a,b,c=map(int,input().split())
for number in range(a,b+1):
    if c%number==0:
        count+=1
print(count)