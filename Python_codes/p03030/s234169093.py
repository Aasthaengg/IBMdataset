n=int(input())
l=[]
for i in range(n):
    x,y=input().split()
    y=int(y)
    l.append([x,-y,i+1])
l.sort()
for i in l:
    print(i[2])
