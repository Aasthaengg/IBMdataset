from itertools import product

n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))
a_sum = set()


for a in product(*((x,0) for x in A)):
    a_sum.add(sum(a))

for m in M:
    if m in a_sum:
        print("yes")
    else:
        print("no")

