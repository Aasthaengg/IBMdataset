a,b,c,d = list(map(int,input().split()))

dx = c-a
dy = d-b
l = []
e=c-dy
f=d+dx


g = e-dx
h = f-dy

print(e,end=" ")
print(f,end=" ")
print(g,end=" ")
print(h,end=" ")