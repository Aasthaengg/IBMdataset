n=int(input())
t=[0]
x=[0]
y=[0]
for i in range(n):
   s=list(map(int,input().split()))
   t.append(s[0])
   x.append(s[1])
   y.append(s[2])

for i in range(n):
    dt=t[i+1]-t[i]
    dx=x[i+1]-x[i]
    dy=y[i+1]-y[i]
    dl=abs(dx)+abs(dy)
    if dl<=dt and dt%2==dl%2:
        continue
    else:
        print("No")
        exit()
print("Yes")
