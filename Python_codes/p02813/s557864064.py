import itertools as it
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

all_num_list = list(it.permutations(range(1,N+1)))
all_num_list.sort()

P_num = all_num_list.index(P)
Q_num = all_num_list.index(Q)

print (abs(P_num-Q_num))