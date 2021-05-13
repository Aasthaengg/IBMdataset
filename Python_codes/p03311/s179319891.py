import collections 

N = int(input())
A = list(map(int,input().split()))
A = sorted([j - (i + 1) for i,j in enumerate(A)])

c = N // 2
a = A[c]
ans = sum([abs(i - a) for i in A])

print(ans)