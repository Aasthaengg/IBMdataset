n=int(input())
p=[]
for i in range(n):
    p.append(int(input()))
#print(p)
p.sort()
#print(p)
sum=0
for i in range(n-1):
    sum+=p[i]
print(int(sum+p[n-1]/2))