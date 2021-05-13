N, K = map(int, input().split())
H = list(map(int, input().split()))

J = [j for j in H if j >= K]

print(len(J))