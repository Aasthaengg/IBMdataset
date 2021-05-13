N = int(input())
A = list(map(int, input().split()))
A.sort()
l = A[N//2-1]
h = A[N//2]
print(h-l)