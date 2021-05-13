from itertools import permutations
N = int(input())
P = tuple(list(map(int,input().split())))
Q = tuple(list(map(int,input().split())))
cnt = 0
for x in permutations(range(1,N+1),N):
    if P==x:
        indP = cnt
    if Q==x:
        indQ = cnt
    cnt += 1
print(abs(indP-indQ))