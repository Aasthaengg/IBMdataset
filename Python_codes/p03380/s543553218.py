import bisect

N = int(input())
a = set(map(int,input().split()))
A = sorted(list(a))
M = max(A)
num = M//2

index = bisect.bisect_right(A,num)

if index > 0 and abs(num - A[index]) > abs(num - A[index-1]):
    index = index-1
#print(index)

if M != A[index]:
    print(M,A[index])
else:
    print(M,A[index-1])