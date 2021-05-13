N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

from itertools import permutations

lis = [i+1 for i in range(N)]
per = permutations(lis,N)

index = 0
for i in per:
    if i == P:
        p_index = index
    if i == Q:
        q_index = index
    index += 1
    
print(abs(p_index-q_index))