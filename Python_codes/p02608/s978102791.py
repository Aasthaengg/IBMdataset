n = int(input())
li = [0]*n
p = int(n**0.5)
for x in range(1,p+1):
    for y in range(1,p+1):
        for z in range(1,p+1):
            k = x**2+y**2+z**2+x*y+y*z+z*x
            if k<=n:
                li[k-1]+=1

print(*li,sep="\n")