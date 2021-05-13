N = int(input())
A = list(map(int,input().split()))

A.sort()
while len(A) > 1:
    for i in range(1,len(A)):
        A[i] %= A[0]
    A = [x for x in A if x != 0]
    A.sort()

print(A[0])