import sys
N,A,B = map(int,input().split())
array = list(map(int,input().split()))

cost = 0
for J in range(len(array)-1):
        walk_cost = (array[J+1] - array[J])*A
        if walk_cost < B:
            cost += walk_cost
        else:
            cost += B
print(cost) 