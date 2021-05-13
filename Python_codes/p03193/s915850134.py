n,a,b = map(int, input().split())
l=[[int(i) for i in input().split()] for i in range(n)] 
c=0
for i,k in l:
    if i>=a and k>=b:
        c+=1
print(c)
