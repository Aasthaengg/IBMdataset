a=[0]*int(input())
r=range(1,99)
for x in r:
    for y in r:
        for z in r:
            n=x*(x+y+z)+y*(y+z)+z*z-1
            if n<len(a):
                a[n]+=1
print(*a)