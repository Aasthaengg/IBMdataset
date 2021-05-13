import collections
N = int(input())
A = collections.Counter(int(T) for T in input().split()).most_common()
Remove = 0
for T in range(0,len(A)):
    if A[T][0]>A[T][1]:
        Remove += A[T][1]
    elif A[T][0]<A[T][1]:
        Remove += A[T][1]-A[T][0]
print(Remove)