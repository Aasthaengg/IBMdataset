import itertools
N = int(input())
num = int(N**0.5)+1

ans = [0]*(N+1)

# for x in range(1,num+1):
#     for y in range(1,num+1):
#         for z in range(1,num+1):

for x,y,z in itertools.product(range(1, num+1), repeat=3):
    fn = x**2 + y**2 + z**2 + x*y + y*z + z*x
    if fn > N:
        continue
    else:
        ans[fn] += 1

for i in range(1,len(ans)):
    print(ans[i])