import collections
N = int(input())
A = collections.Counter(int(input()) for T in range(N)).most_common()
Num = 0
for T in range(len(A)):
    if A[T][1]%2!=0:
        Num += 1
print(Num)