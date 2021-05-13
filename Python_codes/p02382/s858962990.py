import math
N=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
c=[abs(b[i]-a[i]) for i in range(N)]
print(sum(c))
print(math.sqrt(sum([c[i]**2 for i in range(N)])))
print((sum([c[i]**3 for i in range(N)]))**(1/3))
print(max(c))

