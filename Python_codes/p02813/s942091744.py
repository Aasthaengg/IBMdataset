import itertools

N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
l = []
a = 0
b = 0
for i in itertools.permutations(range(1,N+1)):
    l.append(list(i))

for j in l:
    if j == P:
        a = l.index(j)+1
    if j == Q:
        b = l.index(j)+1
print(abs(a-b))