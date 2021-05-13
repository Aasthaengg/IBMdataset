#n=int(input())
a1,a2,a3=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

d1=abs(a2-a1)
d2=abs(a3-a2)
d3=abs(a3-a1)

l=[d1,d2,d3]

l.sort()

print(l[0]+l[1])
