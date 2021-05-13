import itertools
A,B,C=map(int,input().split())
K=int(input())

l=[0,1,2,3,4,5,6,7]

for c  in itertools.product(l, repeat=3):
    if sum(c) == K and A*2**c[0]<B*2**c[1] and B*2**c[1]<C*2**c[2]:
      print("Yes")
      exit(0)
print("No")
