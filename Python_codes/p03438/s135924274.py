N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

cluster_two = 0
cluster_one = 0

for i in range(N):
    if A[i] < B[i]:
        cluster_two += (B[i]-A[i])//2
    elif A[i] > B[i]:
        cluster_one += A[i]-B[i]

if cluster_two >= cluster_one:
    print('Yes')
else:
    print('No')