L,R=map(int,input().split())
R=min(L+2019,R)
m=3000
for x1 in range(L,R):
    for x2 in range(x1+1,R+1):
        if m>(x1*x2)%2019:m=(x1*x2)%2019
print(m)