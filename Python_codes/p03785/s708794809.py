n,capacity,time_limit=map(int,input().split())
a=sorted([int(input()) for _ in range(n)])
c=0
start_num=0

while True:
    if start_num>=n:break
    start_time=a[start_num]
    for x in range(start_num,start_num+capacity):
        if x>=n:break
        if start_time+time_limit>=a[x]:start_num+=1
        else:break
    c+=1

print(c)