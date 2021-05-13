k,n = map(int, input().split())

A = list(map(int, input().split()))

A.append(k+A[0])

road = [A[i+1]-A[i] for i in range(n)]

print(sum(road)-max(road))