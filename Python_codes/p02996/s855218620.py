n=int(input())
lst=[]
for i in range(n):
    a,b=map(int,input().split())
    lst.append([a,b])
lst=sorted(lst,key=lambda x:x[1])
time=0
for i in range(n):
    a,b=lst[i]
    time+=a
    if time>b:
        print("No")
        exit()
print("Yes")