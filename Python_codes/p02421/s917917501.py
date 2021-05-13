n=int(input())
c=[input().split() for i in range(n)]

t=0
h=0

for j in c:
    if j[0]>j[1]:
        t+=3
    elif j[0]<j[1]:
        h+=3
    else:
        t+=1
        h+=1
print(t, h)
