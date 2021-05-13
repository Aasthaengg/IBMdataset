a,b,k = map(int,input().split())
li = []
if k*2 >= b-a+1:
    for i in range(a,b+1):
        li.append(i)
    for i in range(len(li)):
        print(li[i])
else:
    for i in range(k):
        li.append(a+i)
        li.append(b-i)
    li.sort()
    for i in range(len(li)):
        print(li[i])