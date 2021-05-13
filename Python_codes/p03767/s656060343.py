N = int(input())
A = sorted(map(int, input().split()))[::-1]
I = [1+2*i for i in range(N)]
print(sum(A[i] for i in I))