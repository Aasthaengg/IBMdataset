
n=int(input())
g=0
for i in range(1,n+1):
    g+= 0.5*i*(n//i)*((n//i)+1)
print(int(g))