N, A, B = [int(i) for i in input().split()]
X = [int(i) for i in input().split()]
t = 0
for i in range(N-1):
    t += min((X[i+1] - X[i]) * A, B)
print(t)