N=int(input())

a=[0]*10**4

for x in range(1,100):
     for y in range(1,100):
         for z in range(1,100):
             n=(x+y+z)**2-(x*y+y*z+z*x)
             if n<=10000:
                 a[n-1]+=1

for n in range(N):
    print(a[n])





