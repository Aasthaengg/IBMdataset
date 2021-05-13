N, M, X = map(int, input().split())
A = list(map(int, input().split()))

l = [i for i in A if i > X]

l2 = [i for i in A if i < X]

print(min(len(l), len(l2)))