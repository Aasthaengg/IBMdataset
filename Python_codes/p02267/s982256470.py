def linerSearch(A, key):
    for i in A:
        if i == key:
            return 1
    return 0

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
c=0
for j in T:
    if linerSearch(S, j) != 0:
        c += 1
print(c)
