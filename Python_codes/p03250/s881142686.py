A=list(map(int, input().split()))
A.sort(reverse=True)
print(sum(A)+A[0]*9)
