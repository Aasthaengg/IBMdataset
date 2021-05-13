n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
work=[abs(x[i]-y[i]) for i in range(n)]

p1=sum(work)
p2=(sum([x**2 for x in work]))**0.5
p3=(sum([x**3 for x in work]))**(1/3)
p_inf=max(work)

print(p1)
print(p2)
print(p3)
print(p_inf)
