N, T = map(int, input().split())
A = list(map(int,input().split()))
print(max(max(A) - (sum(A) - max(A)) - 1, 0))