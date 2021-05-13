import collections

N = int(input())
A = list(map(int,input().split()))

c = collections.Counter(A)

for i in range(1,N):
    print(c[i])

print(0)