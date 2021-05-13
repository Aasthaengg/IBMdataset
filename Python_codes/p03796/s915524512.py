N = int(input())

po = 1

for i in range(1,N+1):
    # i = 1, 2, 3, ... ,N
    po = po * i % 1000000007


print(po)

