from itertools import permutations

n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))

order = list(permutations(list(range(1,n+1))))
turn_p = order.index(p)
turn_q = order.index(q)

print(abs(turn_p-turn_q))