a,b=map(int,input().split())
count=1
for i in range(2,1000):
    if a-count==b-count-i:
        print(count-a)
        break
    count+=i