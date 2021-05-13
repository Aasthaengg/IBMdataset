k=int(input())
if k%2==0 or k%5==0:
    print(-1)
    exit()
count=0
a=0
while True:
    a=(a*10+7)%k
    count+=1
    if a==0:
        print(count)
        exit()