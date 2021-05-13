import sys
N,A,B = map(int,input().split())
array = list(map(int,input().split()))

if not ( 2 <= N <= 10**5 and 1 <= A <= 10**9 and 1 <= B <= 10**9 ): sys.exit()
for I in range(len(array)):
    if not ( 1 <= array[I] <= 10**9 ): sys.exit()
    if array[I] != array[-1]:
       if not ( array[I] < array[I+1] ): sys.exit()

cost = 0
for J in range(len(array)):
    if array[J] != array[-1]:
        walk_cost = (array[J+1] - array[J])*A
        if walk_cost < B:
            cost += walk_cost
        else:
            cost += B
print(cost) 