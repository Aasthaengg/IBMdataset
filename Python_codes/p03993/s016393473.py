n = int(input())

L = list(map(int,input().split()))

li = set()

for i in range(n):
    a = tuple(sorted([i+1,L[i]]))
    li.add(a)
print(n-len(li))