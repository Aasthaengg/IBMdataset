A = list(map(int,input().split()))
K = int(input())
N = sorted(A)[-1]
print(sorted(A)[0] + sorted(A)[1] +N*2**K)
