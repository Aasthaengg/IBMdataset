n=int(input())
l=[[int(i) for i in input().split()] for _ in range(n)]

a,b,c=0,0,0
for x in range(n):
    pa,pb,pc=l[x]
    a,b,c=pa+max(b,c),pb+max(a,c),pc+max(b,a)

print(max(a,b,c))