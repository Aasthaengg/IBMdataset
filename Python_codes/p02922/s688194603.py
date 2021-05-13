a,b=map(int,input().split())
c=1
count=0
for i in range(20):
    if c>=b:
        break
    c+=a-1
    count+=1
print(count)