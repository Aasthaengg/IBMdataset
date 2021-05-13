k=int(input())
a=list(map(int,input().split()))
l,r=2,2
for i in a[::-1]:
 l,r=((l-1)//i+1)*i,(r//i+1)*i-1
 if l>r:exit(print(-1))
print(l,r)