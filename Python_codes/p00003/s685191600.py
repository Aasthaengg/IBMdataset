a=int(input())
for i in range(a):
    x,y,z=[int(i) for i in input().split() ]
    if (x*x==z*z+y*y)or(y*y==z*z+x*x)or(z*z==x*x+y*y):
        print("YES")
    else:
        print("NO")