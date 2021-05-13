import itertools

N = int(input())
P = [int(x) for x in input().split()]
Q = [int(x) for x in input().split()]

a = 0
b = 0
j = 0
for i in itertools.permutations([int(x+1) for x in range(N)]):
    j += 1
    if(list(i) == P) :
        a = j
    if(list(i) == Q) :
        b = j

print(abs(a-b))