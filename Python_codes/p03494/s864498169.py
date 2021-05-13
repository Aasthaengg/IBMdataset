n=int(input())
*a,=map(int,input().split())
c=0
while all([i%2==0 for i in a]):
    a=[j/2 for j in a]
    c+=1
print(c)