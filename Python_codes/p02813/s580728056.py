import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
num = 0
for i in itertools.permutations(range(1,n+1),n):
    if i == p:
        a = num
    if i == q:
        b = num
    num += 1
print(abs(a-b))