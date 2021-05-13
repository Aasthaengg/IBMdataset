import collections
N = int(input())

A = [0]*N
for i in range(N):
    A[i] = int(input())

#print(collections.Counter(A))
c = collections.Counter(A)
count = 0
for i in c:
    count+=c[i]%2
print(count)