N = int(input())
A = [0]
input_A = list(map(int, input().split()))
A.extend(input_A)
A.append(0)

distances = []

for i in range(N+1):
    distance = abs(A[i+1] - A[i])
    distances.append(distance)

S = sum(distances)

for i in range(1, N+1):
    ans = S - (distances[i-1] + distances[i]) + abs(A[i+1]-A[i-1])
    print(ans)
