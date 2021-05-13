from itertools import product
h,w,k=map(int,input().split())
a=0
c=[[0 if l=='.' else 1 for l in input()] for _ in range(h)]
for i in product([0,1] , repeat=h):
  for j in product([0,1] , repeat=w):
    b=0
    for H,W in product(range(h),range(w)):
      b+=c[H][W]*i[H]*j[W]
    if b == k:
      a+=1
print(a)