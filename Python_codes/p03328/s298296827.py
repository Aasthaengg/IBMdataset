a,b = map(int,input().split())
li = []
for i in range(1,1000):
    li.append(i*(i+1)//2)
difference = b-a
print(li[difference - 2] - a)