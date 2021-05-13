from itertools import permutations

n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
a = -1
b = -1
count = 0
for per in permutations(range(1,n+1)):
    count += 1
    arr = [i for i in per]
    if arr==p:
        a = count
    if arr==q:
        b = count

print(abs(a-b))