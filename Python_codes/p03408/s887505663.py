n=int(input())
blues=[]
for i in range(n):
    blues.append(input())
m=int(input())
reds=[]
for i in range(m):
    reds.append(input())
m=0
for blue in blues:
    x=blues.count(blue)-reds.count(blue)
    m=max(m,x)
print(m)