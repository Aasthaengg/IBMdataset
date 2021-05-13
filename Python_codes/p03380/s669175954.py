N=int(input())
alst=sorted(list(map(int,input().split())))

n=alst.pop()
center=n/2
cost=10**10

for a in alst:
    if abs(a-center)<cost:
        cost=abs(a-center)
        r=a

print('{} {}'.format(n,r))