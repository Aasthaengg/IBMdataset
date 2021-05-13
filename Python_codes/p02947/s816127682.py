import collections
N = int(input())
A = []
for i in range(N):
    s = sorted(input())
    A.append(str(s))
B = collections.Counter(A)
print(sum(i*(i-1)//2 for i in B.values()))