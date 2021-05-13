N, M = map(int, input().split())
A = list(map(int, input().split()))
availability = N
for i in range(M):
    availability -= A[i]

if availability < 0:
    print(-1)
else:
    print(availability)