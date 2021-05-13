n=int(input())
k=int(n**0.5)+1
a=[0 for i in range(n+1)]
for x in range(1,k):
    for y in range(1,k):
        for z in range(1,k):
            g=x*x+y*y+z*z+x*y+y*z+x*z
            if g<=n:
                a[g]+=1
print(*a[1:],sep='\n')