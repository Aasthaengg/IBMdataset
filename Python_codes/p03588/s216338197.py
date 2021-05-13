n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append([a,b])
l.sort(reverse=True)

print(l[0][0]+l[0][1])
