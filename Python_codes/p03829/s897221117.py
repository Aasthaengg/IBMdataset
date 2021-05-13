N, A, B = map(int, input().split())
X = [int(a) for a in input().split()]

print(sum([min((X[i]-X[i-1]) * A, B) for i in range(1, N)]))
