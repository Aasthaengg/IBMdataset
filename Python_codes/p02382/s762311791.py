n=int(input())
x=[int(X) for X in input().split()]
y=[int(Y) for Y in input().split()]
p1,p2,p3,p=0,0,0,[]
for i in range(n):
    p1+=abs(x[i]-y[i])
print(f'{p1:.5f}')
for i in range(n):
    p2+=(abs(x[i]-y[i]))**2
print(f'{p2**(1/2):.5f}')
for i in range(n):
    p3+=(abs(x[i]-y[i]))**3
print(f'{p3**(1/3):.5f}')
for i in range(n):
    p.append(abs(x[i]-y[i]))
print(f'{max(p):.5f}')
