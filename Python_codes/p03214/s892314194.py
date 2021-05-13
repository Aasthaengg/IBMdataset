N = int(input())
a = list(map(int, input().split()))

ave = sum(a)/(N)
index = 0
min_sa = 10000
for i,j in enumerate(a):
    if min_sa > abs(j-ave):
        index = i
        min_sa = abs(j-ave)
print(index)
