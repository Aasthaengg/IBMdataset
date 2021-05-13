n=int(input())
X=[0]+list(map(int,input().split()))+[0]

whole=0
for i in range(n+1):
    whole+=abs(X[i+1]-X[i])

for i in range(n):
    t=whole
    t-=abs(X[i+1]-X[i])+abs(X[i+2]-X[i+1])
    t+=abs(X[i+2]-X[i])
    print(t)