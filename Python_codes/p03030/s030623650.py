n=int(input())
a=[]
for i in range(1,n+1):
    s,t=input().split()
    t=int(t)    
    t=-t
    a.append((s,t,i))
a.sort()
for i in range(n):
    print(a[i][2])