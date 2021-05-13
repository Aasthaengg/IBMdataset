import collections
N = int(input())
A = list(map(int,input().split()))
B = collections.Counter(A)
num = 0
for i in set(A):
    if B[i] > 1:
        num += B[i]*(B[i] - 1)//2
for i in A:
    print(num-B[i]+1)