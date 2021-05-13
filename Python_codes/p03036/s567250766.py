r,D,x= [int(i) for i in input().split()]
def xa(x):
    return r*x-D
for i in range(10):
    ans = xa(x)
    x = ans
    print(ans)