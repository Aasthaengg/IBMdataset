N, A, B = map(int, input().split())

town = list(map(int, input().split()))
diff = [0]*(N+1)
for i in range(1, N):
    diff[i] = town[i] - town[i-1]

sumz = 0
for i in range(1, N+1):
    if diff[i]*A > B:
        sumz += B
    else:
        sumz += diff[i]*A

print(sumz)
