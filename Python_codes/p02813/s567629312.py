import itertools

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

l = [i for i in range(1,n+1)]

cnt = 0
for v in itertools.permutations(l, len(l)):
    if p == list(v):
        pi = cnt
    if q == list(v):
        qi = cnt 
    cnt += 1

print(abs(pi-qi))
