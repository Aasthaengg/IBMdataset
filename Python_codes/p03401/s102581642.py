n=int(input())
l=[0]+list(map(int,input().split()))+[0]
f=lambda x,y:abs(l[x]-l[y])
s=sum(f(i+1,i) for i in range(n+1))
for i in range(n): print(s-f(i+1,i)-f(i+2,i+1)+f(i+2,i))